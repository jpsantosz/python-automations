# Importando a biblioteca matplotlib para criação de gráficos
import matplotlib.pyplot as plt

# Usuário insere seu salário
salario = float(input("Digite seu salário: "))

# A partir da resposta do usuário se obtém os valores de suas finanças (usando a lógica 50-35-15)
gastos_fixos = salario * 0.50
investimentos = salario * 0.35
lazer = salario * 0.15

labels = ["Gastos fixos", "Investimentos", "Lazer"]
sizes = [gastos_fixos, investimentos, lazer]

# Função para formatar os valores no gráfico
def func_definir_valores(pct, allsizes):
    absolute = pct / 100.*sum(allsizes)  # Calcula o valor absoluto
    return f'R$ {absolute:,.2f}'  # Formata o valor com o símbolo de R$ e com 2 casas decimais

fig1, ax1 = plt.subplots()

# Cria-se um gráfico de fatias(pie) e usa os parâmetros definidos anteriormente
ax1.pie(sizes, labels=labels, autopct=lambda pct: func_definir_valores(pct, sizes), shadow=True, startangle=90)

ax1.axis("equal")

plt.show()