# 🏗️ Projeto 1 — E-Commerce Medallion Lakehouse Pipeline

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24+-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-D71F00?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

# 📖 Sobre o Projeto

O **E-Commerce Medallion Lakehouse Pipeline** é uma solução de **Engenharia de Dados** responsável pela construção de um **Data Lakehouse** baseado na **Arquitetura Medallion**, utilizando PostgreSQL e Docker como infraestrutura.

O pipeline transforma dados brutos de e-commerce em informações analíticas organizadas nas camadas **Bronze**, **Silver** e **Gold**, produzindo contratos de dados em formato CSV para consumo pelos demais projetos do ecossistema.

Este projeto representa a **base de toda a arquitetura**, alimentando:

- 🤖 **Projeto 2 — Machine Learning**
- 📊 **Projeto 3 — Dashboard Analytics**

---

# 📑 Índice

- [Arquitetura](#-arquitetura-medallion)
- [Fluxo de Dados](#-fluxo-de-dados)
- [Camadas do Lakehouse](#-camadas-do-lakehouse)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias](#-tecnologias-utilizadas)
- [Instalação](#-instalação)
- [Execução](#-execução)
- [Saídas Geradas](#-saídas-geradas)
- [Integração com os Projetos](#-integração-com-os-projetos)
- [Licença](#-licença)

---

# 🏛️ Arquitetura Medallion

```text
                Dados Brutos
                     │
                     ▼
             ┌───────────────┐
             │    Bronze     │
             │ Dados Originais│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │    Silver     │
             │ Dados Limpos  │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │     Gold      │
             │ Dados Analíticos │
             └───────┬───────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   Projeto 2             Projeto 3
 Machine Learning      Analytics Dashboard
```

---

# 🔄 Fluxo de Dados

```text
CSV / Dados Brutos
        │
        ▼
PostgreSQL (Docker)
        │
        ▼
Bronze Layer
        │
        ▼
Silver Layer
        │
        ▼
Gold Layer
        │
        ▼
Exportação CSV
        │
        ├────────► Projeto 2
        │
        └────────► Projeto 3
```

---

# 🥉🥈🥇 Camadas do Lakehouse

## 🥉 Bronze

Armazena os dados exatamente como foram recebidos.

Características:

- Dados brutos
- Sem transformações
- Histórico completo
- Fonte única da verdade

---

## 🥈 Silver

Responsável pelo tratamento dos dados.

Processos realizados:

- Remoção de duplicidades
- Tratamento de valores nulos
- Conversão de tipos
- Padronização
- Validação
- Regras de qualidade

---

## 🥇 Gold

Camada destinada ao consumo analítico.

Contém:

- KPIs
- Agregações
- Métricas de negócio
- Esquema estrela
- Dados prontos para BI

---

# 🚀 Funcionalidades

## 📥 Ingestão

- Importação de dados
- Persistência no PostgreSQL
- Estruturação das tabelas

---

## 🔄 Transformação

- Limpeza dos dados
- Tratamentos
- Padronizações
- Regras de negócio

---

## 📊 Modelagem Analítica

- Construção da camada Gold
- Esquema Estrela (Star Schema)
- Métricas de vendas
- Indicadores comerciais

---

## 📤 Exportação

O pipeline exporta automaticamente contratos de dados em CSV para integração com outros projetos.

---

# 📂 Estrutura do Projeto

```text
ecommerce-medallion-lakehouse/
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── docker/
│
├── sql/
│
├── src/
│   ├── ingest.py
│   ├── bronze.py
│   ├── silver.py
│   ├── gold.py
│   └── export.py
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python | Pipeline de dados |
| PostgreSQL | Banco de dados |
| Docker | Infraestrutura |
| Pandas | Manipulação de dados |
| SQLAlchemy | ORM |
| SQL | Consultas analíticas |

---

# ⚙️ Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/ecommerce-medallion-lakehouse.git

cd ecommerce-medallion-lakehouse
```

---

## 2. Crie o ambiente virtual

### Windows

```powershell
python -m venv .venv

.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Inicie o PostgreSQL

```bash
docker compose up -d
```

---

# ▶️ Execução

Execute o pipeline completo:

```bash
python src/main.py
```

Ou execute cada etapa individualmente:

```bash
python src/ingest.py
python src/bronze.py
python src/silver.py
python src/gold.py
python src/export.py
```

---

# 📤 Saídas Geradas

Ao final da execução, o pipeline produz arquivos como:

```text
data/gold/

├── vendas_gold_dashboard.csv
├── clientes_gold.csv
└── produtos_gold.csv
```

Esses arquivos representam os contratos de dados utilizados pelos demais projetos.

---

# 🔗 Integração com os Projetos

```text
              Projeto 1
        Medallion Lakehouse
                  │
        Contratos de Dados
                  │
      ┌───────────┴───────────┐
      ▼                       ▼

Projeto 2              Projeto 3
Machine Learning   Analytics Dashboard
```

O Projeto 1 atua como o **produtor central de dados**, fornecendo datasets consistentes para as etapas de Machine Learning e visualização analítica.

---

# 📸 Demonstração

Adicione capturas de tela ou GIFs da execução.

```markdown
docs/lakehouse.png

docs/pipeline.gif
```

Exemplo:

```html
<p align="center">
<img src="docs/lakehouse.png" width="100%">
</p>
```

---

# 🚀 Próximos Passos

- Orquestração com Apache Airflow
- Versionamento de dados
- Incremental Load
- Particionamento
- Testes automatizados
- Data Quality Checks
- Monitoramento de pipelines
- Deploy em ambiente cloud

---

# 👨‍💻 Autor

Projeto desenvolvido para demonstrar a implementação de uma arquitetura moderna de **Data Engineering**, baseada no padrão **Medallion Lakehouse**, integrando ingestão, transformação, modelagem analítica e distribuição de dados para aplicações de Machine Learning e Business Intelligence.

---

# 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

Sinta-se à vontade para utilizar este projeto para estudos, aprendizado e desenvolvimento de portfólio.
