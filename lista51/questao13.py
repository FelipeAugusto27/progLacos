'''
Desenvolver um programa que imprima a tabuada de 3 a 6.
'''

# Processamento e Output
fator1 = 3
fator2 = 1

while fator1 <= 6:
    while fator2<= 10:
        print(f"{fator1}x{fator2}={fator2*fator1}")
        fator2 = fator2 + 1
    fator1 = fator1 + 1
    fator2 = 1