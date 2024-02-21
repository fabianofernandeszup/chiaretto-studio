## About

This action will convert the plugin/action documentation to the new format
with i18n support.

---
## Usage

1. Run the command:

```
stk run action studio/action
```

2. The files below will be unified into `docs/pt_br/doc.md` and `docs/en_us/doc.md`

- `about.md`
- `implementation.md`
- `release-notes@action-version.md`
- `requirements.md`

3. Check if the content was as expected.

4. Run the `stk update doc` command to update your documentation, or publish a new release.