'''
Desenvolver um programa que apresente todos os valores numerico inteiros ímpares situados na faixa de 0 a 20.
Para saber se o número é ímpar, será necessário verificar essa condição com comando if.
Sendo ímpar, mostre-o; se não passe para o próximo passo.
'''

# Processamento
var = 0
while var <= 20:
    if var%2!=0:
        print(var)
    var = var + 1
print("FIM")
