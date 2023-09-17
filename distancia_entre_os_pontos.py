from math import sqrt
xa = float(input("Digite o valor X do ponto A:"))
xb = float(input("Digite o valor X do ponto B:"))
ya = float(input("Digite o valor Y do ponto A:"))
yb = float(input("Digite o valor Y do ponto B:"))
distancia_entre_os_pontos = sqrt((xa - xb)**2 + (ya - yb)**2)
print(f"A distância entre esses pontos é de {distancia_entre_os_pontos :.2f} Dab")
