#Rosolução
MEDIA_REFERENCIA = (150.172) # "Constantes" em Python são convencionalmente escritas em maiúsculas, utilizei uma tupla para garantir a imutabilidade do valor

safras = {
    "2023": 180.421,
    "2024": 200.797,
    "2025": 190.464
}
soma_total = 0

for valor in safras.values():
    soma_total += valor

media = soma_total / len(safras)

# 1. FORMATANDO O LAUDO FINAL PARA O USUÁRIO

print("--- LAUDO DE SAFRA ---\n")
print(f"Período analisado: {len(safras)} anos")
print(f"Média de produtividade: {media:.2f} toneladas")
print(f"Meta de referência: {MEDIA_REFERENCIA} toneladas\n")

# 2. FILTRO DE ANÁLISE DA PRODUTIVIDADE DA CULTURA

if media >= MEDIA_REFERENCIA:
    print(f"Diagnóstico: Produtividade satisfatória. O solo mantém bons índices de rendimento.")

else:
    print(f"Diagnóstico: Atenção: Produtividade abaixo do limiar aceitável. Recomenda-se iniciar a naálise para rotação de culturas.")


