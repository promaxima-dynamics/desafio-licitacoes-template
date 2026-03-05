# Desafio Técnico • Monitor de Preços de Medicamentos (PMVG)
*Stack obrigatória: **Django 4 + Django REST Framework + PostgreSQL + Vue 3 (Composition API) + Pinia + Vite***

---

## 📑 Sumário
1. [Objetivo](#objetivo)
2. [História (Cenário fictício)](#história-cenário-fictício)
3. [Fluxo de participação](#fluxo-de-participação)
4. [Estrutura inicial do projeto](#estrutura-inicial-do-projeto)
5. [Checklist de commits](#checklist-de-commits)
6. [Entregáveis obrigatórios (MVP)](#entregáveis-obrigatórios-mvp)
7. [Diferenciais (pontuação extra)](#diferenciais-pontuação-extra)
8. [Evidências de autoria (obrigatório)](#evidências-de-autoria-obrigatório)
9. [Como testar com Docker](#como-testar-com-docker)
10. [Perguntas conceituais](#perguntas-conceituais)
11. [Critérios de avaliação](#critérios-de-avaliação)

---

## Objetivo
Criar um mini-sistema capaz de **baixar periodicamente** uma planilha pública de referência de preços (formato **XLS**), importar esses dados para PostgreSQL e disponibilizar aos usuários:

*   Busca textual com filtros (fabricante, código interno, faixa de preço, status do produto etc.);
*   Painel de **estatísticas** (menor, maior, média, mediana) para o termo pesquisado;
*   Exportação dos itens selecionados em **XLS**.

A planilha-fonte está disponível na seção **PMVG** (Preço Máximo de Venda ao Governo) de um portal institucional de medicamentos. Os arquivos seguem o padrão:

`https://www.gov.br/anvisa/.../arquivos/xls_conformidade_gov_<DATA>.xls`

**(Exemplo real incluído em `sample_data/`)**

---

## História (Cenário fictício)
A rede de farmácias **VidaMais** pretende participar de compras corporativas e precisa saber, com rapidez, **quais preços de venda estão sendo praticados** para cada medicamento referenciado na planilha PMVG. O time de desenvolvimento recebeu a missão de entregar um painel interno que:

1.  **Importe** a planilha PMVG (fornecida ou baixada);
2.  **Armazene** cada registro em banco, mantendo histórico se possível;
3.  Permita que analistas pesquisem valores, visualizem estatísticas e exportem os itens escolhidos em XLS para negociações.

Você deve entregar esse sistema inicial em **Docker**, usando Django + DRF no back-end e Vue 3 no front-end.

---

## Fluxo de participação
1.  Clique em **"Use this template → Create a new repository"**.
    *   Marque **Private**.
    *   Nome sugerido: `desafio-licitacoes-SEU_NOME`.
2.  Em *Settings → Collaborators*, adicione **`marcossouz`** com permissão **Write**.
3.  Trabalhe sempre em uma branch `develop`.
4.  Ao finalizar **todos** os itens da [Checklist](#checklist-de-commits), abra **Pull Request** `develop → main`.
5.  Aguarde o **GitHub Actions** ficar 🟢 verde — ele executa testes e verificações automáticas.

> Seu repositório permanecerá privado; outros candidatos **não** verão seu código.

---

## Bloco de verificação
*NÃO APAGUE NEM ALTERE — o CI confere a presença deste hash em três arquivos.*

```md
<!--
  *** NÃO REMOVER ESTA CAIXA ***
  VERIFICACAO: 9b12b6f7-4c91-421e-b5a5-ef1a14
-->
```
Esse hash também aparece comentado em:

*   `backend/core/models.py`
*   `frontend/src/App.vue`
*   `backend/core/tests/test_ingest.py`

---

## Estrutura inicial do projeto
```bash
.
├── .github/
│   └── workflows/
│       └── ci.yaml        # Workflow GitHub Actions
├── backend/               # Django project
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models.py      # TODOs marcados + Hash
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── ingest_licitacoes.py # TODO
│   │   ├── serializers.py # TODO
│   │   ├── views.py       # TODO
│   │   ├── urls.py        # TODO
│   │   ├── tests/
│   │   │   └── test_ingest.py # Teste falhando + Hash
│   │   └── README_sources.md # Colunas mínimas
│   ├── settings.py
│   └── manage.py
├── frontend/              # Vue 3 + Vite
│   └── src/
│       └── App.vue        # TODO + Hash
├── sample_data/
│   └── xls_conformidade_gov_20250414_195721251.xls # Arquivo de exemplo
├── scripts/
│   ├── check_commits.sh   # Script de verificação (CI)
│   └── check_hash.sh      # Script de verificação (CI)
├── tests/                 # Testes de integração (opcional)
│   └── test_dummy.py
├── docker-compose.yml     # Postgres + API + SPA
└── README.md              # Este arquivo
```

---

## Checklist de commits
Faça um commit por linha **exatamente** com o prefixo indicado (o CI valida):

| # | O que entregar             | Prefixo na mensagem de commit |
|---|----------------------------|-------------------------------|
| 1 | Modelos + migrations       | `feat(models):`               |
| 2 | Comando `ingest_licitacoes`| `feat(ingest):`               |
| 3 | Endpoints DRF              | `feat(api):`                  |
| 4 | UI de busca + tabela       | `feat(ui):`                   |
| 5 | Exportação XLS             | `feat(export):`               |
| 6 | Refatoração/documentação (opcional) | `refactor:` ou `test:` |

---

## Entregáveis obrigatórios (MVP)

**1. Ingestão de dados:**
*   Implementar o comando `python manage.py ingest_licitacoes <caminho_do_xls>`.
*   O comando deve ler o arquivo XLS (ex: `sample_data/...xls`) e popular o modelo `ItemPMVG`.
*   Mapear **pelo menos** as colunas listadas em `backend/core/README_sources.md`.
*   Deve usar `update_or_create` baseado no `codigo_ggrem` para permitir re-execuções.
*   (Opcional) Adicionar lógica para lidar com múltiplas planilhas ao longo do tempo (versionamento).

**2. API (Django REST Framework):**
*   **Endpoint `GET /api/items/`:**
    *   Listar itens do banco (`ItemPMVG`).
    *   Permitir filtros via query params (ex: `?search=termo`, `?laboratorio=xyz`, `?preco_min=10`, `?preco_max=50`).
    *   Paginação (ex: 100 itens por página).
*   **Endpoint `GET /api/items/stats/`:**
    *   Receber os mesmos filtros de busca da listagem.
    *   Devolver um JSON com estatísticas calculadas sobre os itens filtrados: `{ "min": X, "max": Y, "mean": Z, "median": W }`.

**3. Front-end (Vue 3 + Pinia + Vite):**
*   Tela principal com:
    *   Campo de busca textual.
    *   (Opcional) Filtros adicionais (laboratório, faixa de preço).
    *   Tabela exibindo os resultados da API (`/api/items/`), paginada.
    *   Checkbox em cada linha da tabela para selecionar itens.
    *   Botão "Exportar Selecionados (XLS)" que baixa uma planilha apenas com os itens marcados.
    *   Exibição das estatísticas (`/api/items/stats/`) relacionadas à busca atual (pode ser em um card, tooltip, modal, etc.).

---

## Diferenciais (pontuação extra)
Você não precisa entregar todos os itens abaixo para ser aprovado no desafio.

*   Testes automatizados (backend e/ou frontend).
*   Tratamento robusto de dados sujos (datas inválidas, preços ausentes, texto com espaços extras, etc.).
*   Melhorias de performance (queries otimizadas, paginação eficiente, redução de chamadas).
*   Melhorias de UX (feedback de loading/erro, filtros adicionais, melhor legibilidade da tabela).
*   Logs e observabilidade básica no processo de ingestão.

---

## Evidências de autoria (obrigatório)
Além do código funcional, envie evidências curtas de decisão técnica:

*   Preencha o arquivo `DECISOES.md` com:
    *   3 decisões técnicas relevantes;
    *   1 trade-off (escolha com prós e contras)
    *   1 risco conhecido;
    *   1 melhoria que faria com +2h.
*   Use o template de Pull Request (`.github/pull_request_template.md`) respondendo objetivamente:
    *   o que foi implementado;
    *   o que não foi implementado e por quê;
    *   como validar manualmente.

---

## Como testar com Docker
```bash
# 1. Subir os containers (API, Web, Banco de Dados)
docker-compose up --build -d

# 2. Popular o banco usando o arquivo de exemplo
docker-compose exec api python manage.py ingest_licitacoes sample_data/xls_conformidade_gov_20250414_195721251.xls

# 3. Acessar as aplicações
#    - Frontend (Vue): http://localhost:3000 (ou a porta definida no docker-compose)
#    - Backend API (Django): http://localhost:8000

# 4. Rodar os testes (após implementar as funcionalidades)
docker-compose exec api pytest
# docker-compose exec web npm run test # (ou comando equivalente do frontend)

# 5. Derrubar os containers
docker-compose down -v
```

---

## Perguntas conceituais
Responda diretamente neste `README.md`, abaixo desta seção (máximo 200 palavras no total):

1.  Como você garantiria que os preços importados da planilha permaneçam consistentes e auditáveis no seu banco de dados, mesmo que a Anvisa publique uma nova versão da planilha com correções ou remoções?
2.  Se, em vez de baixar um XLS, você precisasse fazer *scraping* diretamente de um portal web para obter esses dados, quais cuidados tomaria para não sobrecarregar o servidor do portal e evitar bloqueios de IP? Cite duas técnicas.

*(Insira suas respostas aqui)*

---

## Critérios de avaliação (100 pts)

| Item                                                | Pontos |
|-----------------------------------------------------|--------|
| Funcionalidades MVP (backend + frontend)            | 55     |
| Qualidade de código (PEP8/ESLint, clareza, SOLID)   | 20     |
| Clareza técnica (DECISOES.md + descrição de PR)     | 15     |
| Diferenciais (inclui testes automatizados)          | 10     |
| Commits seguindo o padrão e organização do Git      | 5      |
| Respostas às perguntas conceituais                  | 10     |
| **Desclassificação Automática:**                    |        |
| * Hash de verificação ausente/modificado            |        |
| * Commits obrigatórios não encontrados pelo CI      |        |
| * Erros graves no `docker-compose up`               |        |

Boa sorte — valorizamos clareza, qualidade e método! 
