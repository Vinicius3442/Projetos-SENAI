import random

numeros_aleatorios = []

# Esse foi dificil em
for i in range(10):
    numeros_aleatorios.append(random.randint(1, 100))

print("Números aleatórios gerados:", numeros_aleatorios)
print("Números pares:")
for numero in numeros_aleatorios:
    if numero % 2 == 0:
        print(numero)


