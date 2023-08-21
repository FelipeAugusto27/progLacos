'''
Desenvolver um programa que leia um número n qualquer menor ou igual a 50 e apresente o valor obtido da multiplicação
sucessiva de n por 3 enquanto o produto for menor que 250 (nx3; nx3; nx3;...).
'''


# Input
n = int(input("Apresente um valor aleatório de 1 a 50: "))

# Processamento e Output
produto = 1
if n > 50:
    print("Valor Inválido")
else:
    while n < 250:
        print(n)
        n = n * 3
print("FIM")
