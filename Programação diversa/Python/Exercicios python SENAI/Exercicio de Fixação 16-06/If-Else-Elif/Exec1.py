# Vinicius Montuani N° 29

def maior(num1, num2):
    return num1 if num1 > num2 else num2

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

resultado = maior(num1, num2)

print(f"O maior número é o: {resultado}")