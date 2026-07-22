import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 1. Carregar variáveis do .env e conectar ao PostgreSQL
load_dotenv()

user = os.getenv("POSTGRES_USER", "postgres")
password = os.getenv("POSTGRES_PASSWORD", "postgres123")
db = os.getenv("POSTGRES_DB", "lakehouse_db")
port = os.getenv("DB_PORT", "5433")

engine = create_engine(f"postgresql://{user}:{password}@localhost:{port}/{db}")

# 2. Ler os dados higienizados da Camada SILVER
print("📖 Lendo dados higienizados da tabela 'silver.vendas_limpas'...")
df_silver = pd.read_sql("SELECT * FROM silver.vendas_limpas", con=engine)

# ---------------------------------------------------------
# 3. CRIANDO AS TABELAS DIMENSÃO (Contextos)
# ---------------------------------------------------------
print("⭐ Modelando o Star Schema na Camada GOLD...")

# A. Dimensão Cliente
dim_cliente = df_silver[['id_cliente', 'nome_cliente', 'cidade_cliente', 'estado_cliente']].drop_duplicates().reset_index(drop=True)

# B. Dimensão Produto
dim_produto = df_silver[['id_produto', 'nome_produto', 'categoria_produto', 'preco_unitario']].drop_duplicates().reset_index(drop=True)

# C. Dimensão Tempo / Calendário
df_silver['data_venda'] = pd.to_datetime(df_silver['data_venda'])

dim_tempo = pd.DataFrame({'data': df_silver['data_venda'].dt.date.unique()})
dim_tempo['data'] = pd.to_datetime(dim_tempo['data'])
dim_tempo['ano'] = dim_tempo['data'].dt.year
dim_tempo['mes'] = dim_tempo['data'].dt.month
dim_tempo['nome_mes'] = dim_tempo['data'].dt.month_name()
dim_tempo['trimestre'] = dim_tempo['data'].dt.quarter
dim_tempo['dia_semana'] = dim_tempo['data'].dt.day_name()
dim_tempo = dim_tempo.sort_values('data').reset_index(drop=True)

# ---------------------------------------------------------
# 4. CRIANDO A TABELA FATO (Métricas e Chaves)
# ---------------------------------------------------------
df_silver['data_key'] = df_silver['data_venda'].dt.date

fato_vendas = df_silver[[
    'id_venda', 
    'id_cliente',       # Chave para dim_cliente
    'id_produto',       # Chave para dim_produto
    'data_key',         # Chave para dim_tempo
    'quantidade',       # Métrica
    'desconto',         # Métrica
    'valor_total',      # Métrica
    'forma_pagamento', 
    'status_pedido'
]]

# ---------------------------------------------------------
# 5. CARGA NA CAMADA GOLD
# ---------------------------------------------------------
print("💾 Salvando o Star Schema na camada GOLD...")

dim_cliente.to_sql('dim_cliente', con=engine, schema='gold', if_exists='replace', index=False)
dim_produto.to_sql('dim_produto', con=engine, schema='gold', if_exists='replace', index=False)
dim_tempo.to_sql('dim_tempo', con=engine, schema='gold', if_exists='replace', index=False)
fato_vendas.to_sql('fato_vendas', con=engine, schema='gold', if_exists='replace', index=False)

print("🏆 SUCESSO! O Esquema Estrela (dim_cliente, dim_produto, dim_tempo, fato_vendas) está pronto no PostgreSQL!")