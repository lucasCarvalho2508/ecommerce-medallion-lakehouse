# 🚀 E-Commerce Medallion Lakehouse

Este projeto demonstra a construção completa de um **Data Lakehouse para E-Commerce**, desde o provisionamento da infraestrutura com **Docker** até a disponibilização de um **Esquema Estrela (Star Schema)** na camada **Gold** e uma **CLI de consultas analíticas** desenvolvida em Python.

A arquitetura segue o padrão **Medallion Architecture (Bronze → Silver → Gold)**, garantindo:

- ✅ Imutabilidade dos dados brutos
- ✅ Governança de dados
- ✅ Qualidade e padronização
- ✅ Alto desempenho para análises
- ✅ Estrutura preparada para ferramentas de BI

---

# 🏛️ Arquitetura do Projeto

```text
               ┌──────────────────────────────────────────────┐
               │         Dados Brutos (data/vendas.csv)       │
               └──────────────────────┬───────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🟤 CAMADA BRONZE (Raw Zone)                                                 │
│ • Ingestão bruta dos dados                                                  │
│ • Sem alterações de estrutura                                               │
│ • Histórico imutável                                                        │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚪ CAMADA SILVER (Trusted Zone)                                              │
│ • Limpeza de dados                                                          │
│ • Remoção de duplicados                                                     │
│ • Conversão de tipos                                                        │
│ • Padronização dos registros                                                │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🟡 CAMADA GOLD (Refined Zone)                                               │
│ • Modelagem Dimensional                                                     │
│ • Esquema Estrela                                                           │
│ • Fato + Dimensões                                                          │
│ • Consultas otimizadas para BI                                              │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🖥️ CLI Python                                                               │
│ • Consultas analíticas                                                      │
│ • KPIs                                                                      │
│ • Relatórios                                                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas**
- **NumPy**
- **PostgreSQL 15**
- **SQLAlchemy**
- **Psycopg2**
- **Docker**
- **Docker Compose**
- **python-dotenv**
- **Git**
- **GitHub**

---

# 📂 Estrutura do Projeto

```text
ecommerce-medallion-lakehouse/
│
├── data/
│   └── vendas.csv
│
├── src/
│   ├── 01_ingestao_bronze.py
│   ├── 02_limpeza_silver.py
│   ├── 03_modelagem_gold.py
│   └── 04_menu_consultas.py
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Como Executar o Projeto

## 1. Pré-requisitos

Instale:

- Git
- Docker Desktop
- Python 3.10+

---

## 2. Clonar o repositório

```bash
git clone https://github.com/lucasCarvalho2508/ecommerce-medallion-lakehouse.git

cd ecommerce-medallion-lakehouse
```

---

## 3. Criar ambiente virtual

### Windows

```bash
python -m venv .venv

.\.venv\Scripts\Activate.ps1
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 5. Configurar o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto.

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres123
POSTGRES_DB=lakehouse_db
```

---

## 6. Subir o PostgreSQL

```bash
docker compose up -d
```

O banco será iniciado em segundo plano.

---

# 🔄 Executando a Pipeline

Execute os scripts na seguinte ordem.

## Bronze

```bash
python src/01_ingestao_bronze.py
```

Responsável por carregar o arquivo CSV para:

```text
bronze.vendas_raw
```

---

## Silver

```bash
python src/02_limpeza_silver.py
```

Responsável por:

- remover nulos
- remover duplicados
- converter tipos
- padronizar dados

Resultado:

```text
silver.vendas_limpas
```

---

## Gold

```bash
python src/03_modelagem_gold.py
```

Cria o modelo dimensional:

- fato_vendas
- dim_cliente
- dim_produto
- dim_tempo

---

# 📊 Consultas Analíticas

Execute:

```bash
python src/04_menu_consultas.py
```

Menu disponível:

```text
🚀 LAKEHOUSE E-COMMERCE

1️⃣ Total de faturamento por categoria

2️⃣ Top 5 clientes

3️⃣ Evolução mensal do faturamento

4️⃣ Distribuição por forma de pagamento

5️⃣ Ticket médio por estado

0️⃣ Sair
```

---

# ⭐ Modelagem Dimensional

A camada Gold foi construída utilizando **Star Schema**.

## Tabela Fato

### `gold.fato_vendas`

Contém as métricas:

- quantidade
- valor_total
- desconto

e as chaves:

- id_cliente
- id_produto
- id_tempo

---

## Dimensão Cliente

### `gold.dim_cliente`

Contém:

- Nome
- Cidade
- Estado
- Demais atributos cadastrais

---

## Dimensão Produto

### `gold.dim_produto`

Contém:

- Produto
- Categoria
- Preço Unitário

---

## Dimensão Tempo

### `gold.dim_tempo`

Permite análises por:

- Ano
- Mês
- Dia
- Dia da semana

---

# 🎯 Objetivos do Projeto

Este projeto demonstra conceitos de Engenharia de Dados como:

- Arquitetura Medalhão
- ETL/ELT
- Data Lakehouse
- PostgreSQL
- Docker
- Modelagem Dimensional
- Star Schema
- SQL Analítico
- Python para Engenharia de Dados

---

# 👨‍💻 Autor

**Lucas Carvalho**

GitHub:

> https://github.com/lucasCarvalho2508

---

# 📄 Licença

Este projeto foi desenvolvido para fins de estudo e demonstração de conceitos de Engenharia de Dados.readme.md