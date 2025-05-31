import random

numRandom = random.randint(0, 100)
palpite = int(input("Escolha um número entre 0 e 100: "))

while palpite != numRandom:
    print("Você errou!")   
    if palpite < numRandom:
        print("O número é maior que o seu palpite.")
        palpite = int(input("Escolha um número entre 0 e 100: "))
    else:
        print("O número é menor que o seu palpite.")
        palpite = int(input("Escolha um número entre 0 e 100: "))
else:
    print("Você acertou!")
    print(f"O número era {numRandom}.")
