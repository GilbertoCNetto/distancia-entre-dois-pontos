broa = int(input("Quantas broas foram vendidas no dia? "))
paes = int(input("Quantos pães foram vendidos no dia? "))
valor_broas = broa * 1.5
valor_paes = paes * 0.12
total_de_vendas = valor_paes + valor_broas
poupanca = total_de_vendas * 0.1
print(f"O total de broas vendidas foi de {broa}")
print(f"O total de pães vendidos foi de {paes}")
print(f"O total arrecadado dessas vendas foi de {total_de_vendas}")
print(f"E o total a ser colocado na poupança é de {poupanca}")
