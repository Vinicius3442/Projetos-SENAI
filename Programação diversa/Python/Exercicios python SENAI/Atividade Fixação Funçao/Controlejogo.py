import time
import random

def criarPersonagem(nome, vida, classe, ataque, defesa, determinacao):
    personagem = {
        "nome": nome,
        "vida": vida,
        "classe": classe,
        "ataque": ataque,
        "defesa": defesa,
        "determinação": determinacao
    }
    print(f"\nO personagem {nome} foi criado com sucesso!")
    print(f"Classe: {classe} | Vida: {vida} | Ataque: {ataque} | Defesa: {defesa} | Determinação: {determinacao}\n")
    return personagem


def inimigoAleatorio():
    num = random.randint(1, 10)

    inimigos = {
    1: {"nome": "Dragão Vermelho Demoníaco", "vida": 100, "ataque": 40, "defesa": 20, "intimidacao": 30},
    2: {"nome": "Destruidor de Mundos", "vida": 120, "ataque": 45, "defesa": 25, "intimidacao": 40},
    3: {"nome": "Ctulhu", "vida": 200, "ataque": 60, "defesa": 40, "intimidacao": 100},
    4: {"nome": "Xenomorfo", "vida": 110, "ataque": 55, "defesa": 25, "intimidacao": 70},
    5: {"nome": "Sans (Undertale)", "vida": 80, "ataque": 50, "defesa": 20, "intimidacao": 60},
    6: {"nome": "Gaster (Undertale)", "vida": 200, "ataque": 80, "defesa": 40, "intimidacao": 100},
    7: {"nome": "Demonio Abissal", "vida": 180, "ataque": 70, "defesa": 35, "intimidacao": 90},
    8: {"nome": "Dragão Negro", "vida": 180, "ataque": 65, "defesa": 50, "intimidacao": 85},
    9: {"nome": "Demogorgon", "vida": 170, "ataque": 70, "defesa": 40, "intimidacao": 90},
    10: {"nome": "Ultra Apelão de Código Quebrado", "vida": 999, "ataque": 999, "defesa": 999, "intimidacao": 999}
    }


    return inimigos[num]

inimigo = inimigoAleatorio()


# Ações:

def atacar(personagem, inimigo):
    danoPlayer = max(personagem["ataque"] - inimigo["defesa"], 0)
    danoInimigo = max(inimigo["ataque"] - personagem["defesa"], 0)

    inimigo["vida"] -= danoPlayer
    personagem["vida"] -= danoInimigo

    print(f"\nVocê atacou o {inimigo['nome']} causando {danoPlayer} de dano!")
    print(f"O {inimigo['nome']} contra-atacou causando {danoInimigo} de dano!\n")

def fugir(personagem, inimigo):
    if inimigo["intimidação"] > personagem["determinação"]:
        print("\nVocê tentou fugir... mas foi impedido pelo medo!")
        return False
    else:
        print("\nVocê conseguiu fugir com sucesso!")
        return True

# Criar personagem

nome = input("Digite o nome do personagem: ")

print("Digite a classe do personagem")
time.sleep(2)
classeEscolhida = input("\n1) Mago \n2) Guerreiro \n3) Tanque \n4) Paladino\n")

vida = defesa = ataquePoder = determinacao = 0
classeTexto = ""

# Classe

if classeEscolhida == "1":
    classeTexto = "Mago"
    vida = 18
    determinacao = 7
    ataquePoder = 20
    defesa = 10
elif classeEscolhida == "2":
    classeTexto = "Guerreiro"
    vida = 22
    determinacao = 10
    ataquePoder = 13
    defesa = 10
elif classeEscolhida == "3":
    classeTexto = "Tanque"
    vida = 30
    determinacao = 5
    ataquePoder = 5
    defesa = 15
elif classeEscolhida == "4":
    classeTexto = "Paladino"
    vida = 24
    determinacao = 11
    ataquePoder = 10
    defesa = 10
else:
    print("Classe inválida.")
    exit()

personagem = criarPersonagem(nome, vida, classeTexto, ataquePoder, defesa, determinacao)

time.sleep(4)

print(f"Ah não você foi atacado por um {inimigo['nome']}!\n")

time.sleep(3)

while personagem["vida"] > 0 and inimigo["vida"] > 0:
    print(f"\n{personagem['nome']} - Vida: {personagem['vida']} | {inimigo['nome']} - Vida: {inimigo['vida']}")
    
    acao = input("Escolha o que quer fazer:\n1) Atacar\n2) Fugir\n")

    if acao == "1":
        atacar(personagem, inimigo)
        
    elif acao == "2":
        estadoFuga = fugir(personagem, inimigo)
        if estadoFuga:
            break
    
    else:
        print("Opção inválida.")

    if personagem["vida"] <= 0:
        print("\nVocê foi assassinado.")
        break
    
    elif inimigo["vida"] <= 0:
        print(f"\nVocê derrotou o {inimigo['nome']}! Literalmente impossível, tu roubou de alguma forma.")
        break
