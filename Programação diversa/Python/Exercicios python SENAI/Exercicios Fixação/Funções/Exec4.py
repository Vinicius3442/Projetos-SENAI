# Exercício 4: Vinicius Montuani 2°DEV B
import math

def fatorial(num):
    num = math.factorial(num)
    return num

num = int(input("Digite o número a ser calculado em fatorial: "))

resultado = fatorial(num)

print(f"O fatorial de {num} é: {resultado}")