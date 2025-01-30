<!-- 
******************************************

- ESTE É APENAS UM EXEMPLO DE COMO PREENCHER A DOCUMENTAÇÃO DO SEU CONTEUDO. 

- PREENCHA O TEMPLATE COM AS INFORMAÇÕES DO SEU CONTEUDO PARA QUE OUTROS USUÁRIO CONSIGAM UTILIZÁ-LO. ESSA DOCUMENTAÇÃO SERÁ EXPOSTA NA PÁGINA DO CONTEUDO NO PORTAL DA STACKSPOT. 

******************************************
-->
## Nome do Workflow
<!-- Escreva de forma concisa descrevendo seu Workflow. -->

## Requisitos
<!-- [Este é um guia; apague este conteúdo e escreva suas informações fora desta marcação. <!-- ]
- Descreva em uma lista todos os itens e ações necessárias antes de executar seu workflow -->

## Uso
<!-- [Este é um guia; apague este conteúdo e escreva suas informações fora desta marcação. <!-- ]
Adicione os passos para o usuário utilizar seu Workflow:
- Quais são as entradas?
- Quais métodos devemos conhecer?
- Quais são os recursos?
- Adicione as dependências do Workflow, se necessário. -->

## Inputs:                                                                                                   
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Nome                  ┃ Tipo           ┃ Defau… ┃ Patte… ┃ Itens                ┃ Help/Label           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ resource *            │ text           │ Client │ ([A-Z… │                      │ Inform your resource │
│                       │                │        │        │                      │ name (e.g.: Client)  │
│ method *              │ select         │ GET    │        │ ['GET', 'POST',      │ Inform the method of │
│                       │                │        │        │ 'PUT', 'DELETE',     │ the endpoint (e.g.:  │
│                       │                │        │        │ 'PATCH']             │ post or delete)      │
└───────────────────────┴────────────────┴────────┴────────┴──────────────────────┴──────────────────────┘