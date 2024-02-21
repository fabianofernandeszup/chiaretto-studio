## Sobre

Essa action irá converter a documenção do plugin/action para o novo formato 
com suporte a i18n.

---
## Uso

1. Execute o comando:

```
stk run action studio/action
```

2. Os arquivos abaixo, serão unificados em `docs/pt_br/doc.md` e `docs/en_us/doc.md` 

- `about.md`
- `implementation.md`
- `release-notes@action-version.md`
- `requirements.md`

3. Verificar se o conteúdo ficou com esperado.

4. Rodar o comando `stk update doc` para atualizar sua documentação, ou publique uma nova release.