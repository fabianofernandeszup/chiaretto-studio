import requests
from datetime import datetime, timedelta
import re
import os
import json
from stkai import call_code_buddy_chat

CACHE_PATH = os.path.expanduser("~/.stk/.cacheinputs/chiaretto-studio/avaliacao-review-pr-by-user")
CACHE_FILE = os.path.join(CACHE_PATH, "cache.json")

PROMPT = '''Analise a lista de comentários recebidos em um pull request e avalie a qualidade do PR de 0 a 10 baseado na quantidade de comentários e nos tipos de falhas ou erros apontados.

Considere que PRs sem comentários podem não ter sido avaliados e não estarem de fatos bons. O PR precisa ter pelo menos 1 comentário dizendo palavras positivas como OK, LGTM, Aprovado ou etc. Não mencione essa regra de forma explicita.

## Padrão de saida:

📊 Relatório de Avaliação de Qualidade do Pull Request
A qualidade do PR foi avaliada com base nos comentários recebidos durante a revisão. A seguir, estão os principais pontos observados.

🗨️ Quantitativo de Comentários
Total: 31 comentários
Autor predominante: @pedrohrfz (responsável por quase todos os comentários, indicando revisão detalhada)
Observação: presença de comentários repetidos, como “remover”, reforçando a ocorrência de problemas em múltiplos pontos.

⚠️ Tipos de Falhas Apontadas
❌ Código desnecessário – vários pedidos para remover trechos redundantes.
❌ Update handler ausente – apontamentos como “e o update?”.
❌ Uso incorreto de tipos – enums vs. strings, objetos vs. valores esperados.
❌ Instanciação inadequada – criação de objetos em locais impróprios.
❌ Código morto – métodos ou propriedades não utilizados.
❌ Serialização incorreta – problemas com datas e enums.
❌ Conversão ausente – datetime não convertido para string.
❌ Falhas em testes – problemas não detectados pelas automações.
❌ Dependência excessiva de IA – indícios de respostas copiadas.
🔧 Sugestões de refatoração – maior elegância e aderência ao padrão do projeto.
❓ Necessidade duvidosa de eventos ou funcionalidades.
🗑️ Código legado – trechos de versões antigas persistiram no PR.
🔎 Ausência de comentários positivos – Não há manifestações de aprovação ou validação do código.
🔹 Sugestões de boas práticas – código mais exato e aderente ao esperado

📈 Avaliação da Qualidade
- O alto número de comentários indica diversos problemas a serem corrigidos.
- Os erros englobam diferentes categorias: estruturais, lógicos, padrões de projeto e testes insuficientes.
- Alguns problemas são graves, como:
- Uso incorreto de tipos.
- Falhas na conversão de datas.
- Testes ineficazes para capturar erros básicos.

🏅 Nota de Qualidade
Nota sugerida: 2/10
Justificativa:
- O PR apresenta falhas básicas e estruturais, sugerindo:
- Ausência de revisão prévia pelo autor.
- Pouca atenção aos padrões do projeto.
- Testes automatizados ineficazes ou inexistentes.

➡️ Conclusão: Será necessária uma revisão profunda e refatoração significativa antes de considerar a aprovação deste PR.'''

IGNORED_USERS = {"gitbotzup", "snykbotzup"}

def avaliar_pr_conteudo(titulo: str, comentarios: list[str]) -> str:
    """
    Avalia o conteúdo de um PR usando o agente configurado no Code Buddy.

    Args:
        jwt_token: Token JWT do usuário
        titulo: Título do PR
        comentarios: Lista de comentários do PR

    Returns:
        Texto da avaliação ou mensagem padrão caso não haja resposta
    """
    conteudo = f"Prompt: {PROMPT}\r\nTítulo do PR: {titulo}\r\nComentários:\n"
    conteudo += "\n".join(comentarios) if comentarios else "- Nenhum comentário."

    try:
        resposta = call_code_buddy_chat(
            prompt=conteudo
        )
        return resposta.get("answer", "⚠️ Nenhuma avaliação recebida.").strip()
    except Exception as e:
        return f"⚠️ Erro ao avaliar PR: {str(e)}"


def get_pr_status(repo_full, pr_number, headers):
    pr_url = f"https://api.github.com/repos/{repo_full}/pulls/{pr_number}"
    pr_data = requests.get(pr_url, headers=headers, verify=False).json()
    if pr_data.get("merged_at"): return "MERGED"
    return pr_data.get("state", "UNKNOWN").upper()


def listar_prs_e_comentarios(username, token, meses=1):
    headers = {"Accept": "application/vnd.github+json","Authorization": f"token {token}"}
    # 🔹 Data limite
    data_limite = datetime.utcnow() - timedelta(days=meses*30)

    search_url = f"https://api.github.com/search/issues?q=type:pr+author:{username}"
    response = requests.get(search_url, headers=headers, verify=False)
    response.raise_for_status()
    prs = response.json().get("items", [])

    if not prs:
        print(f"\n⚠️ Nenhum PR encontrado para {username}.")
        return

    notas = []
    total_prs = 0
    abaixo_7 = 0
    abaixo_5 = 0
    nota_0 = 0

    for pr in prs:
        pr_created = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        if pr_created < data_limite:
            continue  # ignora PRs antigos

        total_prs += 1
        repo_full = pr["repository_url"].replace("https://api.github.com/repos/", "")
        pr_number = pr["number"]
        pr_title = pr["title"]
        pr_url = pr["html_url"]
        status = get_pr_status(repo_full, pr_number, headers)

        # 🔹 Comentários
        issue_comments = requests.get(f"https://api.github.com/repos/{repo_full}/issues/{pr_number}/comments", headers=headers, verify=False).json()
        review_comments = requests.get(f"https://api.github.com/repos/{repo_full}/pulls/{pr_number}/comments", headers=headers, verify=False).json()
        all_comments = []
        for c in issue_comments + review_comments:
            author = c['user']['login']
            if author not in IGNORED_USERS:
                all_comments.append(f"- {c['body'].strip()} by @{author}")

        # 🔹 Avaliação
        avaliacao = avaliar_pr_conteudo(pr_title, all_comments)

        # 🔹 Extrair Nota sugerida
        nota_match = re.search(r"Nota sugerida[:\s]*([0-9]+)/10", avaliacao)
        nota = int(nota_match.group(1)) if nota_match else 0
        notas.append(nota)
        if nota < 7: abaixo_7 += 1
        if nota < 5: abaixo_5 += 1
        if nota == 0: nota_0 += 1

        # 🔹 Exibir PR
        print("*********************************************************************************************")
        print(f"\n📌 [{repo_full}] PR #{pr_number} [{status}]: {pr_title}")
        print(f"🔗 {pr_url}")
        print("\n".join(all_comments) if all_comments else "- Nenhum comentário encontrado.")
        print(f"\n🤖 Avaliação de qualidade:\n{avaliacao}\n")

    if notas:
        media = sum(notas)/len(notas)
        print("==================================== Resumo Geral ====================================")
        print(f"Total de PRs: {total_prs}")
        print(f"Nota máxima: {max(notas)}/10")
        print(f"PRs com nota abaixo de 7: {abaixo_7}")
        print(f"PRs com nota abaixo de 5: {abaixo_5}")
        print(f"PRs com nota 0: {nota_0}")
        print(f"Nota média geral: {media:.2f}/10")
    else:
        print("\n⚠️ Nenhum PR dentro do período selecionado.")



def carregar_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"USERS": [], "GITHUB_PAT": None}

def salvar_cache(cache):
    os.makedirs(CACHE_PATH, exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4, ensure_ascii=False)

def escolher_usuario(usuarios, padrao=None):
    print("\nSelecione um usuário do GitHub:\n")
    for i, user in enumerate(usuarios, start=1):
        print(f"{i}. {user}")
    print(f"{len(usuarios)+1}. Outro")

    escolha = input("\nDigite o número da opção (padrão 1): ").strip() or "1"
    if escolha.isdigit():
        escolha = int(escolha)
        if 1 <= escolha <= len(usuarios):
            return usuarios[escolha - 1]
        elif escolha == len(usuarios) + 1:
            return input("Usuário do GitHub: ").strip()
    print("❌ Opção inválida.")
    return padrao if padrao else input("Usuário do GitHub: ").strip()


def usuario_existe(username, token=None):
    """
    Verifica se um usuário do GitHub existe.
    """
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    url = f"https://api.github.com/users/{username}"
    resp = requests.get(url, headers=headers, verify=False)
    return resp.status_code == 200


# Execução

def run(metadata):
    # -------- Código principal --------
    cache = carregar_cache()

    # Lista padrão de usuários + cache
    USERS = sorted(
        set(cache.get("USERS", [])),
        key=str.lower
    )

    usuario = escolher_usuario(USERS)

    # 🔹 Validação de existência no GitHub
    if not usuario_existe(usuario, cache.get("GITHUB_PAT")):
        print(f"\n❌ Usuário '{usuario}' não encontrado no GitHub.")
        return  # encerra execução se inválido

    # Perguntar meses (apenas input numérico, default 1)
    meses_input = input("\nDigite quantos meses deseja consultar PRs (padrão 1): ").strip()
    meses = int(meses_input) if meses_input.isdigit() and int(meses_input) > 0 else 1

    # Perguntar GITHUB_PAT (usa cache se vazio)
    pat_input = input("\nDigite o GITHUB_PAT (Enter para usar o último salvo): ").strip()
    if pat_input:
        github_pat = pat_input
        cache["GITHUB_PAT"] = github_pat  # sobrescreve com o novo
    else:
        github_pat = cache.get("GITHUB_PAT")
        if not github_pat:
            github_pat = input("⚠️ Nenhum PAT salvo. Digite o GITHUB_PAT: ").strip()
            cache["GITHUB_PAT"] = github_pat

    # 🔹 Só salva usuário no cache se ele existir
    if usuario not in cache["USERS"]:
        cache["USERS"].append(usuario)

    salvar_cache(cache)

    # Executar com os valores escolhidos
    listar_prs_e_comentarios(usuario, github_pat, meses)