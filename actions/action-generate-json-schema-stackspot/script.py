import os
import json
from typing import List

schemas = [
    'json-schema/plugin/app/v3.json',
    'json-schema/plugin/app/v2.json',
    'json-schema/plugin/infra/v3.json',
    'json-schema/plugin/infra/v2.json',
    'json-schema/action/python/v3.json',
    'json-schema/action/python/v2.json',
    'json-schema/action/shell/v3.json',
    'json-schema/action/shell/v2.json',
    'json-schema/stack/v1.json',
    'json-schema/starter/app/v1.json',
    'json-schema/starter/infra/v1.json',
    'json-schema/workflow/create/v1.json',
    'json-schema/workflow/destroy/v1.json',
    'json-schema/workflow/deploy/v1.json',
    'json-schema/workflow/reusable/v1.json',
    'json-schema/workflow/rollback/v1.json',
    'json-schema/workflow/starter/v1.json',
]


def encontrar_referencias(file_path: str) -> List[str]:
    refs = {}
    cont_refs = 0

    def varredura_recursiva(dados):
        nonlocal cont_refs
        if isinstance(dados, dict):
            for chave, valor in dados.items():
                if chave == "$ref":
                    with open(valor.replace('classpath:', ''), 'r', encoding='utf-8') as f:
                        dados_json = json.load(f)

                    if refs.get(valor) is None:
                        refs[valor] = dados_json
                        cont_refs += 1

                varredura_recursiva(valor)
        elif isinstance(dados, list):
            for item in dados:
                varredura_recursiva(item)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            dados_json = json.load(f)
            varredura_recursiva(dados_json)

        cont = 0
        while True:
            chave = list(refs.keys())[cont]
            with open(chave.replace('classpath:', ''), 'r', encoding='utf-8') as f:
                dados_json_ref = json.load(f)
                varredura_recursiva(dados_json_ref)

            cont += 1
            if cont >= cont_refs:
                break
        return refs
    except Exception as e:
        print(f"Erro ao processar {file_path}: {str(e)}")
        return {}


def substituir_refs(dados):
    if isinstance(dados, dict):
        for chave, valor in dados.items():
            if chave == "$ref" and isinstance(valor, str):
                if valor.startswith("classpath:"):
                    valor_limpo = valor.replace('classpath:json-schema/', '').replace('/', '_').replace('-', '_').replace('.json', '')
                    dados[chave] = f"#/$defs/{valor_limpo}"
            else:
                substituir_refs(valor)
    elif isinstance(dados, list):
        for item in dados:
            substituir_refs(item)
    return dados


def renderizar_schema(schemas):
    os.makedirs('./outputs', exist_ok=True)
    for schema in schemas:
        print('Gerando Schema:', schema)
        try:
            with open(schema, 'r', encoding='utf-8') as f:
                conteudo = json.load(f)

            refs = encontrar_referencias(schema)
            refs_limpo = {}
            for chave, valor in refs.items():
                nova_chave = chave.replace('classpath:json-schema/', '').replace('/', '_').replace('-', '_').replace('.json', '')
                refs_limpo[nova_chave] = valor

            conteudo['$defs'] = refs_limpo
            novo_conteudo = substituir_refs(conteudo)
            caminho_saida = os.path.join('./outputs', schema.replace('/', '-'))
            with open(caminho_saida, 'w', encoding='utf-8') as f:
                f.write(json.dumps(novo_conteudo, indent=2))
            print(f'Arquivo processado: {schema} -> {caminho_saida}')
        except Exception as e:
            print(f'Erro ao processar {schema}: {str(e)}')


renderizar_schema(schemas)

