'''
Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1+2+3+4+...97+98+99+100)
'''

# Processamento e Output
cont = 1
soma = 0
while (cont <= 100):
    soma = soma + cont
    cont = cont + 1
print(f"A soma dos números inteiros de 1 a 100: {soma}")
print("FIM")