# Fluxo de Deploy com GitFlow

Este documento explica o fluxo de deploy de um projeto seguindo o **GitFlow**, uma estratégia de gerenciamento de branches que organiza o desenvolvimento em diferentes estágios.

---

## 📋 Visão Geral do GitFlow

O GitFlow define branches principais e auxiliares para organizar o ciclo de vida do desenvolvimento:

| Branch          | Descrição                                                                 |
|-----------------|---------------------------------------------------------------------------|
| `main`/`master` | Representa o código em produção (versões estáveis).                       |
| `develop`       | Base para integração de novas funcionalidades (próxima release).          |
| `feature/*`     | Branches para desenvolver novas funcionalidades.                          |
| `release/*`     | Branches para preparação de uma nova versão (testes finais).              |
| `hotfix/*`      | Branches para correções críticas em produção (urgentes).                  |

---

## 🚀 Fluxo de Deploy

### 1. **Desenvolvimento (Ambiente de Desenvolvimento)**
- **Branch:** `develop`
- **Processo:**
  - Os desenvolvedores criam branches `feature/*` a partir de `develop`.
  - Após conclusão da feature, fazem merge em `develop` via Pull Request (PR).
  - O ambiente de desenvolvimento é atualizado automaticamente a partir de `develop` (via CI/CD).

### 2. **Preparação para Release (Ambiente de Staging)**
- **Branch:** `release/*` (ex: `release/v1.2.0`)
- **Processo:**
  - Crie uma branch `release/*` a partir de `develop`.
  - Testes finais são realizados no ambiente de staging (QA, testes de integração, etc.).
  - Correções são feitas diretamente na branch `release/*`.
  - Após aprovação, faça merge da `release/*` em `main` e `develop`.

### 3. **Produção (Ambiente de Produção)**
- **Branch:** `main`/`master`
- **Processo:**
  - Após merge da `release/*` em `main`, gere uma tag semântica (ex: `v1.2.0`).
  - O deploy em produção é acionado a partir da tag ou da branch `main` (via CI/CD).
  - **Observação:** Apenas código em `main` é implantado em produção.

### 4. **Hotfixes (Correções Emergenciais)**
- **Branch:** `hotfix/*` (ex: `hotfix/login-bug`)
- **Processo:**
  - Crie uma branch `hotfix/*` a partir de `main`.
  - Corrija o bug e faça merge em `main` e `develop`.
  - Gere uma nova tag (ex: `v1.2.1`) para deploy em produção.

---

## 📈 Diagrama do Fluxo

```mermaid
graph LR
  subgraph Features
    A[feature/novo-componente] --> B(merge em develop)
  end

  subgraph Release
    C[release/v1.2.0] --> D(Testes em staging)
    D --> E(merge em main e develop)
  end

  subgraph Hotfix
    F[hotfix/login-bug] --> G(merge em main e develop)
  end

  main[(main)] --> H[Deploy em produção]
  develop --> I[Deploy em desenvolvimento]
```

## 🛠️ Exemplo de Cenário
- Nova Funcionalidade:
  - Branch: feature/user-auth (criada a partir de develop).
  - Merge em develop após revisão.
  - CI/CD atualiza o ambiente de desenvolvimento.

- Preparação para Release:
  - Branch release/v1.3.0 é criada a partir de develop.
  - Testes em staging: correções são feitas na release/v1.3.0.
  - Merge em main (tag v1.3.0) e develop.

- Deploy em Produção:
  - CI/CD detecta a tag v1.3.0 em main e implanta em produção.
 
- Hotfix Crítico:
  - Bug em produção: cria-se hotfix/auth-error.
  - Correção é feita e merge em main (tag v1.3.1) e develop.
  - Deploy imediato em produção.