# Vinicius Montuani N° 29

def calculadora(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2
    else:
        return "Operador inválido"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operador = input("Digite o operador (+  -  *  /): ")

resultado = calculadora(num1, num2, operador)

print(f"O resultado da operação é: {resultado}")