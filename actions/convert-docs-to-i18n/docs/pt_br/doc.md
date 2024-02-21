## Antes de usar esta Action

- Descreva em uma lista todos os itens e ações necessárias antes de usar a Ação.
- Quando não houver ordem nas etapas, use uma lista não ordenada.
- Se os passos estiverem em ordem, use uma lista ordenada (lista numerada).

Veja o exemplo:

### Etapas não ordenadas

#### Pré-requisito

- Faça a ação X
- Crie o arquivo de configuração
- Renomeie o arquivo **`.env`**.

### Passos ordenados

#### Pré-requisito

1. Instalar dependências
2. Crie o arquivo de configuração
3. Crie a pasta **`template`**.
---
## Adicione o nome da Action aqui! (exemplo: action-doc-template)

Escreva uma descrição clara e breve do conteúdo da sua Action. Responda perguntas como:

- O que as Actions fazem?
- Se necessário, o que o Actions não fazem.
Isso evita interpretações ambíguas e é mais fácil para os usuários entenderem.

Veja um exemplo:

> Esta Action contém instruções de como preencher as informações para usar Plugins na plataforma StackSpot.
---
## Implementação

Descreva todos os passos para usar a Action:

- Preencher entradas
- Quais métodos usar
- Quais são os recursos?
- E se necessário, adicione outros recursos que dependem do tipo da sua Action.

Veja um exemplo:

Na pasta do seu aplicativo, execute o **`action-doc-template`** para preencher os arquivos abaixo:

1. Execute o comando:

```
stk run action /Users/Home/action-doc-template
```

2. Preencha suas informações de ação seguindo os exemplos de modelo de arquivo:

- `about.md`
- `implementation.md`
- `release-notes@action-version.md`
- `requirements.md`
---
# Release Notes 1.0.0

As releases notes devem incluir os seguinte itens:

- Um cabeçalho de introdução e uma breve visão geral das mudanças.
- Uma explicação clara dos usuários afetados.
- Alterações nas notas de versão anteriores.
- Aprimoramentos de recursos ou novos recursos/funcionalidades.
- Problemas corrigidos.
- Problemas/impedimentos/dependências em andamento. Adicione um plano de como as mudanças acontecerão.

Veja um exemplo:

# Alterações do action-doc-template v1.0.0

O action-doc-template v1.0.0 adiciona instruções e exemplos sobre como escrever a documentação para Plugins e Actions na StackSpot.

## Novas funcionalidades

- Foi adicionado um modelo para os seguintes documentos da Action:

    - `about.md`
    - `requirements.md`
    - `implementation`
    - `release-notes@action-version.md`

## Ajustes e Correções

- Corrigido o erro de digitação do modelo da Action.

## Mudanças

- Foram alteradas as funções da Action.
---
## Usage
This action can be used to ...