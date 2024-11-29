# Importa as bibliotecas necessárias:
# pandas para manipulação de dados.
# matplotlib.pyplot para visualização de gráficos.
import pandas as pd
import matplotlib.pyplot as plt

# Lê um arquivo CSV chamado "advertising.csv" e armazena os dados em um DataFrame.
tabela = pd.read_csv("advertising.csv", sep=",")

# Calcula o total gasto em cada meio de propaganda e vendas, somando os valores das respectivas colunas:
valor_gasto_tv = round(tabela["TV"].sum(), 2)
valor_gasto_radio = round(tabela["Radio"].sum(), 2)
valor_gasto_jornal = round(tabela["Jornal"].sum(), 2)
valor_gasto_vendas = round(tabela["Vendas"].sum(), 2)

print("Total gasto em TV's: " + str(valor_gasto_tv))
print("Total gasto em Radio: " + str(valor_gasto_radio))
print("Total gasto em Jornal: " + str(valor_gasto_jornal))
print("Total gasto em Vendas: " + str(valor_gasto_vendas))

labels = ["TV", "Radio", "Jornal", "Vendas"]
sizes = [valor_gasto_tv, valor_gasto_radio, valor_gasto_jornal, valor_gasto_vendas]

# Cria um gráfico de barras para exibir os valores das categorias.
plt.bar(labels, sizes)
plt.show()