def boasVindas(nome, idade):
    if idade > 59:
        print("Seu atendimento é prioritario")
    else:
        print("Seu atendimento não é prioritario")
    
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
            
boasVindas(nome, idade)