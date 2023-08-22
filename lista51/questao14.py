'''
Desenvolver um programa que calcule o fatorial de 15. Ou seja, 5!. Desta forma, temos que 5! = 5. 4. 3. 2. 1. ou
5! 1. 2. 3. 4. 5, equivalente a 120
'''

# Processamento e Output
cont = 1
acumulador = 1
while cont <= 5:
    print(acumulador)
    acumulador = cont * acumulador
    cont = cont + 1
print(f"{acumulador}")
print("FIM")
