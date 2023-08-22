'''
Fazer um programa que pergunte e aguarde resposta com y ou n
'''

print("GAME OVER")
while True:
    print("Continue? [Y]/[N]")
    resposta = input()
    if resposta == "Y":
        print("Reloading map...")
        break
    elif resposta == "N":
        print("Leaving to the main menu...")
        break
    else:
        print("INVALID RESPONSE")
