# Colunas mínimas a mapear na planilha PMVG

| Coluna no XLS         | Campo no modelo    | Observações          |
|-----------------------|--------------------|----------------------|
| `PRODUTO`             | `descricao`        | texto completo       |
| `LABORATÓRIO`         | `laboratorio`      | fabricante           |
| `CÓDIGO GGREM`        | `codigo_ggrem`     | identificador único |
| `DATA DE PUBLICAÇÃO`  | `data_homologacao` | converter para date  |
| `PMVG Sem Impostos`   | `valor_unitario`   | decimal(14,4)        |

Você pode incluir outras colunas se achar relevantes (tarja, regime de preço, etc.), mas essas cinco são obrigatórias para os testes automáticos. 