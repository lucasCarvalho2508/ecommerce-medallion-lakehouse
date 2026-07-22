import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 1. Carregar variáveis de ambiente do arquivo .env
load_dotenv()

user = os.getenv("POSTGRES_USER", "postgres")
password = os.getenv("POSTGRES_PASSWORD", "postgres123")
db = os.getenv("POSTGRES_DB", "lakehouse_db")
port = os.getenv("DB_PORT", "5433")

# 2. Conectar ao PostgreSQL local
engine = create_engine(f"postgresql://{user}:{password}@localhost:{port}/{db}")

# 3. Gerar os dados brutos de simulação (Planilha Suja)
print("🎲 Gerando dados brutos simulados...")
np.random.seed(42)
random.seed(42)

qtd_registros = 100

clientes = [
    (101, "Ana Silva", "São Paulo", "SP"),
    (102, "bruno costa", "rio de janeiro", "rj"),
    (103, "Carla Souza", "Belo Horizonte", "MG"),
    (104, "Diego Lima", "Curitiba", "PR"),
    (105, "Elena Ramos", "Porto Alegre", "RS")
]

produtos = [
    (201, "Notebook Gamer", "Eletrônicos", 4500.00),
    (202, "Smartphone 5G", "Eletrônicos", 2500.00),
    (203, "Cadeira Ergonômica", "Móveis", 1200.00),
    (204, "Teclado Mecânico", "Acessórios", 350.00),
    (205, "Mouse Sem Fio", "Acessórios", 150.00)
]

forma_pagamento = ["Cartão de Crédito", "PIX", "pix", "Boleto", "Boleto Bancário"]
status_pedido = ["Concluído", "CANCELADO", "Em Processamento", None]
data_inicio = datetime(2026, 1, 1)

dados = []
for i in range(1, qtd_registros + 1):
    id_venda = 1000 + i
    if i in [15, 30]:  # Inserindo id duplicado propositalmente
        id_venda = 1005 

    cliente = random.choice(clientes)
    produto = random.choice(produtos)
    
    num_dias = random.randint(0, 180)
    data_venda = (data_inicio + timedelta(days=num_dias)).strftime("%Y-%m-%d %H:%M:%S")
    if i % 12 == 0:
        data_venda = (data_inicio + timedelta(days=num_dias)).strftime("%d/%m/%Y")

    quantidade = random.choice([1, 2, 3, -1, None])
    preco_unitario = produto[3]
    valor_desconto = random.choice([0.0, 10.0, 50.0, np.nan, 9999.0])
    
    dados.append({
        "id_venda": id_venda,
        "data_venda": data_venda,
        "id_cliente": cliente[0],
        "nome_cliente": cliente[1],
        "cidade_cliente": cliente[2],
        "estado_cliente": cliente[3],
        "id_produto": produto[0],
        "nome_produto": produto[1],
        "categoria_produto": produto[2],
        "preco_unitario": preco_unitario,
        "quantidade": quantidade,
        "desconto": valor_desconto,
        "forma_pagamento": random.choice(forma_pagamento),
        "status_pedido": random.choice(status_pedido)
    })

df_bruto = pd.DataFrame(dados)

# 4. Enviar os dados brutos para a camada Bronze no Postgres
print("🚀 Inserindo dados na tabela 'bronze.vendas_raw'...")
df_bruto.to_sql(
    name='vendas_raw',
    con=engine,
    schema='bronze',
    if_exists='replace',
    index=False
)

print("✅ SUCESSO! Carga na Camada Bronze finalizada com 100 registros brutos.")