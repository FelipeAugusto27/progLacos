'''
Elaborar um programa que apresente um valor de uma potência de uma base qualquer (variável b) elevada a um expoente
qualquer (variável e), ou seja b^e (sem usar math.pow)
'''

# Input
b = int(input("Insira um valor para a base: "))
e = int(input("Insira um valor para o expoente: "))
'''
# Processamento e Output (com **)
print(f"{b} elevado a {e} equivale a: {b**e}")
'''

# Processamento e Output (de cabeça)
contagem = 1
acumu = 1
while e >= contagem:
    acumu = acumu * b
    contagem = contagem + 1
print(f"{b} elevado a {e} equivale a: {acumu}")
print("FIM")
