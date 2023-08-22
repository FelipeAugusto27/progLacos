'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o menor
número que foram digitados, além da média entre todos os números digitados pelo usuário. A inserção de números deve parar
quando o número digitar o número -1, e este número -1 não deve ser considerado nem como maior, nem como menor, e nem
na contagem da média.
'''

# Input
num = float(input("Digite um valor: "))
# Processamento
maior = num
menor = num
div = 0
acum = 0
while num != -1:
    div = div + 1
    acum = acum + num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    num = float(input("Digite outro valor: "))

# Output
if menor == -1:
    print("Encerrando...")
else:
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Média dos valores: {acum/div} ")
print("FIM")
