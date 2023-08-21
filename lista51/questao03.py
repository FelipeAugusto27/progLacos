'''
Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200
'''
import math

# Processamento e Output
num = 15
while num < 201:
    quadrado = math.pow(num, 2)
    print(f"O quadrado de {num} é {quadrado:.0f}")
    num = num + 1
print("FIM")
