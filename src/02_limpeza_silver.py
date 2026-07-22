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

# 2. EXTRACT INTERNO: Ler os dados brutos da Camada BRONZE
print("📖 Lendo dados brutos da tabela 'bronze.vendas_raw'...")
df = pd.read_sql("SELECT * FROM bronze.vendas_raw", con=engine)

# ---------------------------------------------------------
# 3. TRANSFORM: Regras de Limpeza, Padronização e Negócio
# ---------------------------------------------------------
print("🧹 Aplicando regras de limpeza na Camada SILVER...")

# Rule A: Remover duplicatas de id_venda
df = df.drop_duplicates(subset=['id_venda']).copy()

# Rule B: Padronizar textos (Title Case e Upper Case)
df['nome_cliente'] = df['nome_cliente'].astype(str).str.title().str.strip()
df['cidade_cliente'] = df['cidade_cliente'].astype(str).str.title().str.strip()
df['estado_cliente'] = df['estado_cliente'].astype(str).str.upper().str.strip()

# Rule C: Padronizar Formas de Pagamento
df['forma_pagamento'] = df['forma_pagamento'].astype(str).str.strip()
mapa_pagamento = {
    'pix': 'PIX',
    'Pix': 'PIX',
    'Boleto Bancario': 'Boleto',
    'Boleto Bancário': 'Boleto'
}
df['forma_pagamento'] = df['forma_pagamento'].replace(mapa_pagamento)

# Rule D: Normalizar coluna de data
df['data_venda'] = pd.to_datetime(df['data_venda'], format='mixed', errors='coerce')

# Rule E: Tratar números e remover anomalias (Outliers/Valores Negativos)
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce')
df = df[df['quantidade'] > 0]  # Remove nulos e quantidades negativas

df['desconto'] = pd.to_numeric(df['desconto'], errors='coerce').fillna(0.0)
df.loc[df['desconto'] > 500, 'desconto'] = 0.0  # Zera o desconto outlier de 9999.0

# Rule F: Criar coluna calculada de Valor Total Líquido
df['valor_total'] = (df['quantidade'] * df['preco_unitario']) - df['desconto']

# ---------------------------------------------------------
# 4. LOAD INTERNO: Salvar os dados limpos na Camada SILVER
# ---------------------------------------------------------
print("💾 Salvando dados limpos na tabela 'silver.vendas_limpas'...")
df.to_sql(
    name='vendas_limpas',
    con=engine,
    schema='silver',
    if_exists='replace',
    index=False
)

print(f"✨ SUCESSO! Camada Silver finalizada com {len(df)} registros higienizados.")