import pandas as pd

# Ler o arquivo CSV
vendas = pd.read_csv("vendas.csv")

# Mostrar as primeiras linhas
print("=== Primeiras linhas do dataset ===")
print(vendas.head())

# Estatísticas gerais
print("\n=== Estatísticas gerais ===")
print(vendas.describe())

# Total de vendas por produto
total_produto = vendas.groupby("Produto")["Valor"].sum()
print("\n=== Total de vendas por produto ===")
print(total_produto)

# Salvar resumo em CSV
total_produto.to_csv("resumo_vendas.csv")
print("\nResumo de vendas salvo em 'resumo_vendas.csv'.")
