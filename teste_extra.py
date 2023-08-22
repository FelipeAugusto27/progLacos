'''
Fazer um programa que pergunte e aguarde resposta com Y ou N repita a pergunta se escrito errado
'''

print("GAME OVER")
while True:
    resposta = input("Continue? [Y]/[N] \n")
    if resposta == "Y":
        print("Reloading map...")
        break
    elif resposta == "N":
        print("Leaving to the main menu...")
        break
    else:
        print("INVALID RESPONSE")
