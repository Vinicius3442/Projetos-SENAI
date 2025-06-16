# Vinicius Montuani N°29

import random

numero_secreto = random.randint(1, 50)
tentativa = 0

while True:
    palpite = int(input("Adivinhe o número entre 1 e 50: "))
    tentativa += 1
    if palpite < numero_secreto:
        print("Maior!")
    elif palpite > numero_secreto:
        print("Menor!")
    else:
        print(f"Acertou em {tentativa} tentativas!")
        break