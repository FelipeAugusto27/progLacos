'''
Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500.
Utilize um laço que efetue a variação de 2 em 2
'''

# Processamento e Output
var = 0
acumulador = 0
while var <= 500:
    acumulador = acumulador + var
    var = var + 2
print(f"Valor acumulado: {acumulador}")
print("FIM")
