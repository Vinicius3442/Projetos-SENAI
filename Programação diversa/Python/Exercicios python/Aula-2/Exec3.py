import random
import os

numRandom = random.randint(0, 10)
palpite = int(input("Escolha um número entre 0 e 10: "))

if (palpite != numRandom):
    print("Vitória!!!")
else:

