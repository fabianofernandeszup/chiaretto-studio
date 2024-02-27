import os
import shutil
import re
import ruamel.yaml

def clean_filename(filename):
    # Remover caracteres especiais e a extensão .md ou .MD do nome do arquivo
    cleaned_name = re.sub(r'[^a-zA-Z0-9]', ' ', os.path.splitext(os.path.split(filename)[1])[0])
    return cleaned_name.capitalize()

# Função para abrir um arquivo YAML
def abrir_arquivo_yaml(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        # Use a classe SafeLoader para carregar o arquivo YAML
        return ruamel.yaml.YAML(typ='safe').load(arquivo)

# Função para editar um arquivo YAML e manter a identação original
def editar_arquivo_yaml(caminho_arquivo, dados_editados):
    # Carregar o arquivo YAML com a classe RoundTripLoader para manter a identação original
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados_originais = ruamel.yaml.YAML(typ='rt').load(arquivo)

    # Atualizar os dados originais com os dados editados
    dados_originais.update(dados_editados)

    # Escrever os dados de volta no arquivo mantendo a identação original
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        yml = ruamel.yaml.YAML(typ='rt')
        yml.indent(mapping=2, sequence=4, offset=2)
        yml.dump(dados_originais, arquivo)

def verificar_e_modificar_yaml(nome_diretorio):
    arquivos_validos = {'action.yaml', 'plugin.yaml'}
    
    arquivos_encontrados = [arquivo for arquivo in os.listdir(nome_diretorio) if arquivo in arquivos_validos]

    if not arquivos_encontrados:
        print(f'Nenhum arquivo válido encontrado no diretório {nome_diretorio}.')
        return

    for nome_arquivo in arquivos_encontrados:
        print("Conteúdo encontrado: ", os.path.join(nome_diretorio, nome_arquivo))
        verificar_e_unificar_docs(nome_diretorio)

        caminho_arquivo = os.path.join(nome_diretorio, nome_arquivo)

        conteudo = abrir_arquivo_yaml(caminho_arquivo)

        if 'spec' in conteudo:
            spec = conteudo['spec']
            # Remover itens existentes
            spec.pop('about', None)
            spec.pop('release-notes', None)
            spec.pop('usage', None)
            spec.pop('requirements', None)
            spec.pop('implementation', None)
            
            specList = list(spec.items())

            # Adicionar novos itens
            novo_elemento = {
                    'pt-br': 'docs/pt-br/doc.md',
                    'en-us': 'docs/en-us/doc.md'
                }

            specList.insert(1, ('docs', novo_elemento))

            conteudo['spec'] = dict(specList)

            if conteudo['schema-version'] == "V1":
                conteudo['schema-version'] = "v2"

        editar_arquivo_yaml(caminho_arquivo, conteudo)

def verificar_e_unificar_docs(caminho):
    # Criar a pasta docs, se não existir
    os.makedirs(os.path.join(caminho, 'docs'), exist_ok=True)

    # Criar as pastas pt_br e en_us dentro da pasta docs
    os.makedirs(os.path.join(caminho, 'docs', 'pt-br'), exist_ok=True)
    os.makedirs(os.path.join(caminho, 'docs', 'en-us'), exist_ok=True)

    # Criar o conteúdo dos arquivos doc.md nas pastas pt_br e en_us
    file_content = {}

    # Docs Antigos
    docs = [
        os.path.join(caminho, 'docs', 'requirements.md'),
        os.path.join(caminho, 'docs', 'about.md'),
        os.path.join(caminho, 'docs', 'implementation.md'),
        os.path.join(caminho, 'docs', 'release-notes.md'),
        os.path.join(caminho, 'docs', 'usage.md')
        ]

    # Ler o conteúdo dos arquivos requirements.md, about.md, implementation.md e release-notes.md
    for filename in docs:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines and not lines[0].startswith('#'):
                    # Adicionar uma linha com "# " seguido do nome do arquivo
                    cleaned_name = clean_filename(filename)
                    lines.insert(0, f"## {cleaned_name}\n")
                elif len(lines) == 0:
                    cleaned_name = clean_filename(filename)
                    lines.insert(0, f"## {cleaned_name}\n")
                
                content = ''.join(lines).strip()
                
                if content:
                    file_content[filename] = content
                else:
                    print(f"O arquivo {filename} está vazio. Pulando para o próximo.")
        except FileNotFoundError:
            print(f"O arquivo {filename} não foi encontrado. Pulando para o próximo.")

    # Escrever o conteúdo nos arquivos doc.md nas pastas pt_br e en_us dentro da pasta docs
    for lang in ['pt-br', 'en-us']:
        path = os.path.join(caminho, 'docs', lang, 'doc.md')
        with open(path, 'w', encoding='utf-8') as file:
            for idx, (filename, content) in enumerate(file_content.items()):
                file.write(content)
                if idx < len(file_content) - 1:  # Adicionar "---" apenas se não for o último conteúdo
                    file.write('\n---\n')

    # Remover os arquivos .md na raiz da pasta docs
    md_files = [f for f in os.listdir(os.path.join(caminho, 'docs')) if f.endswith('.md')]
    for md_file in md_files:
        os.remove(os.path.join(caminho, 'docs', md_file))

    # Copiar os demais arquivos e pastas para os diretórios docs/en_us/ e docs/pt_br/
    for item in os.listdir(os.path.join(caminho, 'docs')):
        if item not in ['en-us', 'pt-br']:
            source_path = os.path.join(caminho, 'docs', item)
            dest_path_en_us = os.path.join(caminho, 'docs', 'en-us', item)
            dest_path_pt_br = os.path.join(caminho, 'docs', 'pt-br', item)

            if os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path_en_us, ignore=shutil.ignore_patterns('en-us', 'pt-br'))
                shutil.copytree(source_path, dest_path_pt_br, ignore=shutil.ignore_patterns('en-us', 'pt-br'))
            else:
                shutil.copy2(source_path, dest_path_en_us)
                shutil.copy2(source_path, dest_path_pt_br)

    # Remover todos os arquivos e diretórios restantes no diretório docs, exceto os diretórios en_us e pt_br
    for item in os.listdir(os.path.join(caminho, 'docs')):
        item_path = os.path.join(caminho, 'docs', item)
        if item not in ['en-us', 'pt-br']:
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

def run(metadata):    
    if os.path.isfile('action.yaml') or os.path.isfile('plugin.yaml'):
        print("Existe um plugin ou action nesse diretório.")
        verificar_e_modificar_yaml('.')
    else:
        print("Não existe um plugin ou action nesse diretório, procurando em diretórios um nível abaixo..")
        for item in os.listdir('.'):
            item_path = os.path.join('.', item)
            if os.path.isdir(item_path):
                print('Verificando diretório: ', item_path)
                verificar_e_modificar_yaml(item_path)

    