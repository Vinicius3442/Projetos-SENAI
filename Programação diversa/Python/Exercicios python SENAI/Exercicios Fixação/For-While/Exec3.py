# Exercício 3: Vinicius Montuani 2°DEV B

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

numAray = [num1, num2, num3, num4, num5]

soma = 0

for i in numAray:
    soma += i

print(f"A soma dos números ({numAray}) é: {soma}")