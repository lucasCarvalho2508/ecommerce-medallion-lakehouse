# 🛒 E-Commerce Medallion Lakehouse & Analytics

Este projeto implementa uma arquitetura de **Lakehouse de Dados** end-to-end baseada na **Arquitetura Medalhão (Bronze, Silver e Gold)** para um ambiente de E-Commerce.

A solução abrange desde o consumo de dados brutos em ambiente containerizado via Docker até a modelagem dimensional (Star Schema) e visualização de KPIs analíticos no Metabase.

---

## 🏗️ Arquitetura da Solução

O fluxo de dados segue o padrão Medalhão para garantir governança, qualidade e integridade das análises:

1. **Bronze (Raw Zone)**: Ingestão dos dados brutos de vendas no PostgreSQL sem tratamento prévio de qualidade.
2. **Silver (Trusted Zone)**: Aplicação de regras de higienização, filtros de validação e remoção de dados inconsistentes ou nulos.
3. **Gold (Refined Zone)**: Estruturação dos dados higienizados em um **Esquema Estrela (Star Schema)** composto por tabelas Fato e Dimensão para consumo analítico.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Python 3.10
* **Manipulação & Conectividade**: Pandas, SQLAlchemy, psycopg2
* **Banco de Dados**: PostgreSQL 15
* **Infraestrutura & Containerização**: Docker & Docker Compose
* **Visualização de Dados & BI**: Metabase

---

## 📊 Modelagem de Dados (Camada Gold)

* **`fato_vendas`**: Contém as métricas quantitativas e financeiras de vendas (`valor_total`, `quantidade`, `desconto`) ligadas às chaves dimensionais.
* **`dim_cliente`**: Informações cadastrais e localização do cliente.
* **`dim_produto`**: Catálogo e categorias de produtos.
* **`dim_tempo`**: Atributos temporais para análise de sazonalidade e tendências.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Docker e Docker Compose instalados
* Python 3.10+ instalado

### Passos para Execução:

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/ecommerce-medallion-lakehouse.git
   cd ecommerce-medallion-lakehouse
   ```

2. **Criar o arquivo de variáveis de ambiente `.env`:**
   ```powershell
   Set-Content -Path .env -Value "POSTGRES_USER=postgres`nPOSTGRES_PASSWORD=postgres123`nPOSTGRES_DB=lakehouse_db`nDB_PORT=5433"
   ```

3. **Subir os containers (PostgreSQL + Metabase):**
   ```bash
   docker compose up -d
   ```

4. **Configurar o ambiente virtual Python e instalar dependências:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

5. **Executar a Pipeline de Dados (Bronze → Silver → Gold):**
   ```powershell
   python src/01_ingestao_bronze.py
   python src/02_limpeza_silver.py
   python src/03_modelagem_gold.py
   ```

6. **Acessar o Dashboard no Metabase:**
   Acesse no navegador: `http://localhost:3000`
