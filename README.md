
```markdown
# 🚀 E-Commerce Medallion Lakehouse

Este projeto apresenta a construção completa de um **Data Lakehouse de E-Commerce**, cobrindo desde o provisionamento da infraestrutura containerizada com Docker até a entrega de um **Esquema Estrela (Star Schema)** na camada Gold e uma **CLI de Consultas Analíticas** em Python.

A arquitetura foi projetada seguindo o padrão da **Arquitetura Medalhão (Bronze, Silver e Gold)**, garantindo imutabilidade dos dados brutos, governança, qualidade de dados e alta performance para análises.

---

## 🏛️ Arquitetura e Fluxo dos Dados

A pipeline processa os dados de vendas através de três camadas isoladas dentro do banco PostgreSQL:

```text
               ┌──────────────────────────────────────────────┐
               │         Dados Brutos (data/vendas.csv)       │
               └──────────────────────┬───────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🟤 CAMADA BRONZE (Raw Zone)                                                 │
│ • Ingestão bruta sem alteração de esquema ou tipagem.                       │
│ • Garante rastreabilidade, histórico imutável e reprocessabilidade.         │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚪ CAMADA SILVER (Trusted Zone)                                              │
│ • Limpeza de nulos críticos (IDs e valores ausentes) e remoção de duplicados.│
│ • Padronização e conversão de tipos de dados (Datas, Numbers, Strings).    │
│ • Tabela única desnormalizada, ideal para auditoria e consumo de Data Science.│
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🟡 CAMADA GOLD (Refined Zone)                                               │
│ • Modelagem Dimensional no formato Esquema Estrela (Star Schema).            │
│ • Separação em Tabela Fato (fato_vendas) e Dimensões (cliente, produto, tempo).│
│ • Estrutura otimizada para consultas analíticas e consumo de BI.            │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🖥️ INTERFACE CLI (Terminal Python)                                           │
│ • Menu interativo que se conecta à Gold e executa consultas SQL de KPIs.    │
└─────────────────────────────────────────────────────────────────────────────┘

```

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem de Programação:** Python 3.10+
* **Manipulação e Análise de Dados:** Pandas, NumPy
* **Banco de Dados / Data Warehouse:** PostgreSQL 15 (via Docker Container)
* **ORM / Conectividade:** SQLAlchemy, Psycopg2
* **Containerização e Infraestrutura:** Docker, Docker Compose
* **Gerenciamento de Ambientes:** `python-dotenv`
* **Versionamento:** Git, GitHub

---

## 📁 Estrutura do Repositório

```text
ecommerce-medallion-lakehouse/
├── data/
│   └── vendas.csv             # Base de dados bruta inicial
├── src/
│   ├── 01_ingestao_bronze.py  # Ingestão do CSV para a camada Bronze (raw)
│   ├── 02_limpeza_silver.py   # Higienização e qualidade de dados na Silver
│   ├── 03_modelagem_gold.py   # Construção do Star Schema na Gold
│   └── 04_menu_consultas.py   # CLI interativa para consulta de KPIs na Gold
├── .env.example               # Exemplo de configuração das variáveis de ambiente
├── .gitignore                 # Arquivos ignorados pelo controle de versão
├── docker-compose.yml         # Configuração da infraestrutura do PostgreSQL
├── README.md                  # Documentação completa do projeto
└── requirements.txt           # Lista de dependências do Python

```

---

## 📖 Passo a Passo: Do Zero às Consultas Analíticas

Siga o tutorial abaixo para subir o ambiente, executar as pipelines e consultar o banco de dados.

### 1️⃣ Pré-requisitos

Certifique-se de ter instalado em sua máquina:

* [Git](https://git-scm.com/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (em execução)
* [Python 3.10+](https://www.python.org/)

---

### 2️⃣ Clonar o Repositório e Configurar o Ambiente Virtual

Abra o terminal e execute:

```bash
# Clonar o repositório
git clone [https://github.com/lucasCarvalho2508/ecommerce-medallion-lakehouse.git](https://github.com/lucasCarvalho2508/ecommerce-medallion-lakehouse.git)
cd ecommerce-medallion-lakehouse

# Criar o ambiente virtual (Python)
python -m venv .venv

# Ativar o ambiente virtual:
# No Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# No Linux/Mac:
source .venv/bin/activate

# Instalar as dependências do projeto
pip install -r requirements.txt

```

---

### 3️⃣ Configurar as Variáveis de Ambiente (`.env`)

Crie um arquivo chamado **`.env`** na raiz do projeto (mesmo diretório do `docker-compose.yml`) utilizando as configurações abaixo:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres123
POSTGRES_DB=lakehouse_db

```

---

### 4️⃣ Subir a Infraestrutura com Docker

Inicie o container do banco de dados PostgreSQL rodando em segundo plano:

```bash
docker compose up -d

```

> **Verificação:** O container `postgres_lakehouse` estará ativo e mapeado na porta **5433** da sua máquina local.

---

### 5️⃣ Executar as Pipelines de Dados (Bronze ➔ Silver ➔ Gold)

Com o banco de dados ativo, rode os scripts da pasta `src/` em sequência para construir o Lakehouse:

#### Passagem 1: Carga Bruta (Bronze)

Lê o arquivo `data/vendas.csv` e carrega os dados brutos na tabela `bronze.vendas_raw`:

```bash
python src/01_ingestao_bronze.py

```

#### Passagem 2: Higienização e Qualidade (Silver)

Aplica regras de tratamento, remoção de registros nulos/duplicados e tipagem correta, gerando a tabela `silver.vendas_limpas`:

```bash
python src/02_limpeza_silver.py

```

#### Passagem 3: Modelagem Dimensional (Gold)

Transforma a tabela desnormalizada da Silver em um **Esquema Estrela** completo na camada Gold:

```bash
python src/03_modelagem_gold.py

```

---

### 6️⃣ Consultando os Dados na Camada Gold (CLI Interativa)

Para realizar análises nos dados modelados sem precisar abrir um cliente SQL externo, execute a CLI interativa no terminal:

```bash
python src/04_menu_consultas.py

```

A interface exibirá o menu abaixo para navegação rápida:

```text
──────────────────────────────────────────────────
🚀 LAKEHOUSE E-COMMERCE - CONSULTAS ANALÍTICAS (GOLD)
──────────────────────────────────────────────────
1️⃣ Total de Faturamento e Vendas por Categoria de Produto
2️⃣ Top 5 Clientes que Mais Gastaram
3️⃣ Faturamento Mensal (Evolução Temporal)
4️⃣ Distribuição de Vendas por Formato de Pagamento
5️⃣ Ticket Médio por Estado do Cliente
0️⃣ Sair
──────────────────────────────────────────────────

```

---

## 📊 Detalhes da Modelagem Dimensional (Camada Gold)

O esquema estrela na camada Gold é estruturado para otimizar *queries* analíticas de negócio:

* **`gold.fato_vendas`**: Tabela central contendo métricas (`quantidade`, `valor_total`, `desconto`) e chaves estrangeiras (`id_cliente`, `id_produto`, `id_tempo`).
* **`gold.dim_cliente`**: Atributos cadastrais e localização dos compradores.
* **`gold.dim_produto`**: Catálogo de produtos, preços unitários e categorias.
* **`gold.dim_tempo`**: Calendário de datas para inteligência temporal (ano, mês, dia, dia da semana).

```

```