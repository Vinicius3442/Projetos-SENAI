def validar_idade(idade):
    CNH = False
    if idade >= 18:
        CNH = True
    else:
        CNH = False
    return CNH

idade_input = int(input("Bem vindo a validação de idade para retirada da CNH\nDigite sua idade para continuar: "))
CNH_trueorfalse = validar_idade(idade_input)
if CNH_trueorfalse == True:
    print(f"O usuário possui idade válidada para tirar a CNH ({idade_input})")
else:
    print(f"O usuário não possui idade válidada para tirar a CNH ({idade_input})")
input("Pressione ENTER para finalizar o programa")