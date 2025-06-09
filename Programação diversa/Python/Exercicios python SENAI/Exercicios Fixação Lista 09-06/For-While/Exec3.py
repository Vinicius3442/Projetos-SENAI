import  random

numRandom = random.randint(1, 10)

while True:
    numUser = int(input("Adivinhe o número entre 1 e 10: "))
    if numUser == numRandom:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Tente novamente.")