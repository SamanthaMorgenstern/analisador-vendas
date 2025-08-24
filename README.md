# 📊 Analisador de Vendas

Projeto simples em **Python** que lê um CSV de vendas, gera estatísticas e salva um resumo de vendas por produto.

## 🚀 Como usar
1. Clone o repositório: `git clone https://github.com/SamanthaMorgenstern/analisador-vendas.git`

2. Entre na pasta: `cd analisador-vendas`

3. Execute o programa: `python analisador.py`

## ✨ Exemplo de uso
=== Primeiras linhas do dataset ===
   Produto  Quantidade  Valor
0   Caneta         10    2.5
1  Caderno          5   15.0
2  Mochila          2  120.0
3   Caneta         15    3.0
4  Caderno          7   16.0

=== Estatísticas gerais ===
        Quantidade       Valor
count     5.000000    5.000000
mean      7.800000   31.700000
std       5.239482   54.413020
min       2.000000    2.500000
25%       5.000000    3.000000
50%       7.000000   15.000000
75%      10.000000   16.000000
max      15.000000  120.000000

=== Total de vendas por produto ===
Produto
Caneta      5.5
Caderno    31.0
Mochila   120.0
Name: Valor, dtype: float64

Resumo de vendas salvo em 'resumo_vendas.csv'.


📌 Tecnologias 

Python 3
Pandas

📄 Licença 

Open-source

