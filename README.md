# Desafio Técnico • Monitor de Preços de Licitações Públicas  
*Stack obrigatória: **Django 4 + Django REST Framework + PostgreSQL + Vue 3 (Composition API) + Pinia + Vite***  

---

## 📑 Sumário
1. [Objetivo](#objetivo)  
2. [Fluxo de participação](#fluxo-de-participação)  
3. [Estrutura inicial do projeto](#estrutura-inicial-do-projeto)  
4. [Checklist de commits](#checklist-de-commits)  
5. [Requisitos funcionais](#requisitos-funcionais)  
6. [Como testar com Docker](#como-testar-com-docker)  
7. [Perguntas conceituais](#perguntas-conceituais)  
8. [Critérios de avaliação](#critérios-de-avaliação)  

---

## Objetivo
Construir um mini-sistema que **captura itens homologados de licitações públicas**, armazena esses dados em banco e permite que o usuário:
- Pesquise **valores unitários** por descrição, órgão ou UF.  
- Veja **estatísticas** (mínimo, máximo, média, mediana).  
- Exporte resultados selecionados para **planilha XLS**.

---

## Fluxo de participação
1. Clique em **“Use this template ➜ Create a new repository”**.<br>
   – Marque **Private**.<br>
   – Nome sugerido: `desafio-licitacoes-SEU_NOME`.  
2. Nas *Settings ➜ Collaborators* do seu repositório, adicione **`github.com/<AVALIADOR>`** com permissão **Write**.  
3. Trabalhe sempre em uma branch `develop`.  
4. Ao finalizar **todos** os itens da [Checklist](#checklist-de-commits), abra **Pull Request** `develop → main`.  
5. Aguarde o **GitHub Actions** ficar 🟢 verde — ele executa testes e verificações automáticas.

> **Observação**  
> Seu repositório permanecerá privado; outros candidatos **não** verão seu código.

---

## Bloco de verificação  
*NÃO APAGUE NEM ALTERE — o CI confere a presença deste hash em três arquivos.*

```md
<!--
  *** NÃO REMOVER ESTA CAIXA ***
  VERIFICACAO: 9b12b6f7-4c91-421e-b5a5-ef1a14
-->
Ele também está comentado em:

backend/core/models.py

frontend/src/App.vue

tests/test_ingest.py

Estrutura inicial do projeto
bash
Copiar
Editar
.
├── backend/               # Django project (configurado)
│   └── core/
│       ├── models.py      # TODOs marcados
│       ├── management/
│       │   └── commands/ingest_licitacoes.py  # TODO
│       └── tests/         # alguns testes falham de propósito
├── frontend/              # Vue 3 + Vite (Hello World)
│   └── src/App.vue        # TODO
├── tests/                 # integração end-to-end (quebrando)
├── docker-compose.yml     # Postgres + API + SPA
└── README.md              # este arquivo
Checklist de commits
Faça um commit por linha com o prefixo indicado; o CI valida.


#	O que entregar	Mensagem (git commit -m)
1	Modelos + migrations	feat(models): criar estrutura inicial
2	Comando ingest_licitacoes	feat(ingest): importar dados de licitações
3	Endpoints DRF	feat(api): listar itens e estatísticas
4	UI de busca + tabela	feat(ui): tela de consulta
5	Exportação XLS	feat(export): botão exportar seleção
6	Refatoração + testes OK	refactor: ajustes finais ou test: cobertura completa
Requisitos funcionais
1. Ingestão de dados
Executar python manage.py ingest_licitacoes --dias 30

Gravar campos: descricao, orgao, uf, data_homologacao, valor_unitario.

Fonte: escolha uma entre [Compras.gov.br Dados Abertos], [Painel de Preços ME], ou [Portal da Transparência] (detalhes em backend/core/README_sources.md).

2. API

Endpoint	Função
GET /api/items/	lista + filtros: texto, órgão (UASG), UF, período, valor min/máx
GET /api/items/stats/?q=termo	devolve JSON {min, max, mean, median}
3. Front-end
Campo de busca e filtros.

Tabela paginada (100 linhas).

Checkbox de seleção e botão Exportar XLS.

Exibir estatísticas em tooltip ou modal.

4. Testes
Backend: ≥ 5 unitários.

Frontend: ≥ 2 de componente (Vitest/Jest).

Como testar com Docker
bash
Copiar
Editar
# Subir tudo
docker-compose up --build

# Popular banco (30 dias)
docker-compose exec api python manage.py ingest_licitacoes --dias 30
SPA em http://localhost:3000, API em http://localhost:8000.

Perguntas conceituais
Responda neste README, abaixo desta seção, em até 200 palavras:

Como garantir que os preços capturados hoje permaneçam auditáveis caso a fonte altere ou exclua dados?

Cite duas técnicas para evitar IP ban ao coletar dados de portais públicos e por que elas funcionam.

Critérios de avaliação (100 pts)

Item	Pontos
Funcionalidades completas	35
Qualidade de código (pep8/eslint, tipagem, docstrings)	20
Docker compose funcional	10
Testes automatizados	10
Commits & organização	10
README final + respostas	10
CI verde	5
Desclassificação automática
• Hash de verificação ausente <br> • Commits obrigatórios faltantes <br> • Docker ou testes quebrados

