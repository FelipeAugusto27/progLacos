'''
Desenvolver um programa que apresente todos os números divísiveis por 4 que sejam menores que 200.
Para saber se o número é divisível por 4 será necessário verificar a lógica desta condição com o comando if.
Sendo divisível, mostre-o, não sendo, passe para o próximo. A variável que controla o controlador deve ser iniciada com
valor 1.
'''

# Processamento e Output
var = 1
while var < 200:
    if var%4 == 0:
        print(f"{var} é divisível por 4")
    var = var + 1
print("FIM")
