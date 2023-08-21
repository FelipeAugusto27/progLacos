'''
Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser impressa no seguinte
Formato: Considerando como exemplo o fornecimento do número 2
2.1=2
2.2=4...
'''

# Input
random = int(input("Apresente um valor aleatório: "))

# Processamento e Output
fator = 0
while fator <= 10:
    resultado = random * fator
    print(f"{random}*{fator}={resultado}")
    fator = fator + 1
print("FIM")
