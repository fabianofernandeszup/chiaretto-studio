
## Manual de Modificações para Desenvolvedores

Este manual descreve as alterações necessárias em uma aplicação para ajustar variáveis e lógicas de acordo com os requisitos especificados. Siga as instruções abaixo para realizar as modificações.

---

### Alterações na **Data Division**

#### Seção: `AL0LGFIE-ENTV2`
- **Variável**: `CGCCDN-ENTV2`
  - **Código Original**:
    ```cobol
    05    CGCCDN-ENTV2        PIC  9(014) VALUE ZEROS.
    ```
  - **Código Sugerido**:
    ```cobol
    05    CGCCDN-ENTV2        PIC  X(014) VALUE SPACES.
    ```
  - **Explicação**: Alteração do tipo de dado de numérico para alfanumérico para suportar caracteres não numéricos.

---

#### Seção: `AL0LGFIE-ENTV3`
- **Variável**: `CGCCDN-ENTV3`
  - **Código Original**:
    ```cobol
    05    CGCCDN-ENTV3        PIC  9(014) VALUE ZEROS.
    ```
  - **Código Sugerido**:
    ```cobol
    05    CGCCDN-ENTV3        PIC  X(014) VALUE SPACES.
    ```
  - **Explicação**: Alteração do tipo de dado de numérico para alfanumérico para suportar caracteres não numéricos.

---

#### Seção: `AL0LGFIE-ENTV4`
- **Variável**: `CGCCDN-ENTV4`
  - **Código Original**:
    ```cobol
    05    CGCCDN-ENTV4        PIC  9(014) VALUE ZEROS.
    ```
  - **Código Sugerido**:
    ```cobol
    05    CGCCDN-ENTV4        PIC  X(014) VALUE SPACES.
    ```
  - **Explicação**: Alteração do tipo de dado de numérico para alfanumérico para suportar caracteres não numéricos.

---

#### Seção: `AL0LGFIE-ENTV5`
- **Variável**: `CGCCDN-ENTV5`
  - **Código Original**:
    ```cobol
    05    CGCCDN-ENTV5        PIC  9(014) VALUE ZEROS.
    ```
  - **Código Sugerido**:
    ```cobol
    05    CGCCDN-ENTV5        PIC  X(014) VALUE SPACES.
    ```
  - **Explicação**: Alteração do tipo de dado de numérico para alfanumérico para suportar caracteres não numéricos.

---

#### Seção: `WORKING-STORAGE`
- **Variável**: `WCGCCDN`
  - **Código Original**:
    ```cobol
    01  WCGCCDN                       PIC  9(14)  VALUE ZEROS.
    ```
  - **Código Sugerido**:
    ```cobol
    01  WCGCCDN                       PIC  X(14)  VALUE SPACES.
    ```
  - **Explicação**: Alteração do tipo de dado de numérico para alfanumérico para suportar caracteres não numéricos.

---

### Alterações na **Procedure Division**

#### Seção: `RT-CONSISTE-ENTRADAV2`
- **Variável**: `CGCCDN-ENTV2`
  - **Código Original**:
    ```cobol
    153200     IF      CGCCDN-ENTV2    NOT   NUMERIC OR                     0IGFI08
    153300             CGCCDN-ENTV2    EQUAL ZEROS                          0IGFI08
    ```
  - **Código Sugerido**:
    ```cobol
    153200     IF      CGCCDN-ENTV2    EQUAL SPACES OR                     0IGFI08
    153300             CGCCDN-ENTV2    EQUAL "00000000000000"                          0IGFI08
    ```
  - **Explicação**: Ajuste na lógica condicional para verificar se a variável é alfanumérica e se é igual a espaços em vez de zeros.

---

### Observações Finais

- Certifique-se de testar todas as alterações em um ambiente de homologação antes de aplicar em produção.
- Caso encontre inconsistências ou dúvidas durante a implementação, entre em contato com o responsável técnico do projeto.

---