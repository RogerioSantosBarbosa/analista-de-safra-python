import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. CARREGAMENTO DOS DADOS
tabela = pd.read_csv("dados_safra.csv")
tabela_milho = tabela[tabela['cultura'] == 'Milho']

# 2. SEPARAÇÃO DO CÉREBRO (O que é causa e o que é efeito?)
# X (Maiúsculo) = As Causas (Características do solo e clima)
X = tabela_milho[['solo_n', 'chuva_mm']]

# y (minúsculo) = O efeito (O que queremos prever: a colheita)
y = tabela_milho['producao_ton']

# 3. TREINAMENTO (A hora em que a IA estuda o CSV)
modelo = LinearRegression() #Criamos um cérebro "em branco"
modelo.fit(X, y) # Comando fit: "Estude o X e o y e encontre o padrão matemático"

# 4. A PREVISÃO (O teste no mundo real)
# Imagine que o agricultor preencheu o formulário dizendo que o solo hoje tem 41 de Nitrogênio e a previsão é de 520mm de chuva.
novo_cenario = pd.DataFrame({'solo_n': [41], 'chuva_mm': [520]})

previsao = modelo.predict(novo_cenario)

print("\n--- TESTE DO MOTOR DE INTELIGÊNCIA ARTIFICIAL ---")
print(f"Cenário inserido: 41 de Nitrogênio e 520mm de chuva.")
print(f"Previsão exata da IA para a próxima colheita: {previsao[0]:.2f} toneladas\n")


           