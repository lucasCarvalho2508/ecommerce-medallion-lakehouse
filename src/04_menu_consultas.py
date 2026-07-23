import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# 1. Carregar variáveis de ambiente
load_dotenv()
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5433/{os.getenv('POSTGRES_DB')}"
engine = create_engine(DATABASE_URL)

def executar_consulta(query, titulo):
    """Executa a query SQL e exibe o resultado formatado no terminal."""
    print(f"\n=======================================================")
    print(f"📊 {titulo.upper()}")
    print(f"=======================================================")
    try:
        df = pd.read_sql(query, engine)
        if df.empty:
            print("⚠️ Nenhum dado encontrado.")
        else:
            print(df.to_string(index=False))
    except Exception as e:
        print(f"❌ Erro ao executar consulta: {e}")
    print("=======================================================\n")

def menu():
    while True:
        print("\n" + "─"*50)
        print("🚀 LAKEHOUSE E-COMMERCE - CONSULTAS ANALÍTICAS (GOLD)")
        print("─"*50)
        print("1️⃣ Total de Faturamento e Vendas por Categoria de Produto")
        print("2️⃣ Top 5 Clientes que Mais Gastaram")
        print("3️⃣ Faturamento Mensal (Evolução Temporal)")
        print("4️⃣ Distribuição de Vendas por Formato de Pagamento")
        print("5️⃣ Ticket Médio por Estado do Cliente")
        print("0️⃣ Sair")
        print("─"*50)
        
        opcao = input("Escolha uma opção (0-5): ").strip()

        if opcao == '1':
            query = """
                SELECT 
                    p.categoria_produto,
                    COUNT(f.id_venda) AS total_vendas,
                    SUM(f.quantidade) AS total_itens_sold,
                    ROUND(CAST(SUM(f.valor_total) AS numeric), 2) AS faturamento_total
                FROM gold.fato_vendas f
                JOIN gold.dim_produto p ON f.id_produto = p.id_produto
                GROUP BY p.categoria_produto
                ORDER BY faturamento_total DESC;
            """
            executar_consulta(query, "Faturamento por Categoria de Produto")

        elif opcao == '2':
            query = """
                SELECT 
                    c.nome_cliente,
                    c.estado_cliente,
                    COUNT(f.id_venda) AS quantidade_compras,
                    ROUND(CAST(SUM(f.valor_total) AS numeric), 2) AS total_gasto
                FROM gold.fato_vendas f
                JOIN gold.dim_cliente c ON f.id_cliente = c.id_cliente
                GROUP BY c.nome_cliente, c.estado_cliente
                ORDER BY total_gasto DESC
                LIMIT 5;
            """
            executar_consulta(query, "Top 5 Clientes por Valor de Compra")

        elif opcao == '3':
            query = """
                SELECT 
                    t.ano,
                    t.mes,
                    COUNT(f.id_venda) AS total_vendas,
                    ROUND(CAST(SUM(f.valor_total) AS numeric), 2) AS faturamento_mes
                FROM gold.fato_vendas f
                JOIN gold.dim_tempo t ON f.id_tempo = t.id_tempo
                GROUP BY t.ano, t.mes
                ORDER BY t.ano, t.mes;
            """
            executar_consulta(query, "Evolução do Faturamento Mensal")

        elif opcao == '4':
            query = """
                SELECT 
                    forma_pagamento,
                    COUNT(id_venda) AS quantidade_transacoes,
                    ROUND(CAST(SUM(valor_total) AS numeric), 2) AS total_movimentado
                FROM gold.fato_vendas
                GROUP BY forma_pagamento
                ORDER BY total_movimentado DESC;
            """
            executar_consulta(query, "Distribuição por Formato de Pagamento")

        elif opcao == '5':
            query = """
                SELECT 
                    c.estado_cliente,
                    COUNT(DISTINCT c.id_cliente) AS total_clientes,
                    ROUND(CAST(AVG(f.valor_total) AS numeric), 2) AS ticket_medio
                FROM gold.fato_vendas f
                JOIN gold.dim_cliente c ON f.id_cliente = c.id_cliente
                GROUP BY c.estado_cliente
                ORDER BY ticket_medio DESC;
            """
            executar_consulta(query, "Ticket Médio por Estado")

        elif opcao == '0':
            print("\n👋 Saindo da CLI de Consultas. Até mais!\n")
            break
        else:
            print("\n⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()