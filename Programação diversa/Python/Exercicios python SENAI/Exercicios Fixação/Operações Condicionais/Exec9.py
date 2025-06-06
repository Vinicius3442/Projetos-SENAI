# Exercício 9: Vinicius Montuani 2°DEV B

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

operacao = input('Digite a operação (+, -, *, /): ')

if operacao == '+':
    resultado = num1 + num2
    
elif operacao == '-':
    resultado = num1 - num2
    
elif operacao == '*':
    resultado = num1 * num2
    
elif operacao == '/':
    resultado = num1 / num2
    
else:
    resultado = 'Operação inválida'

print('O resultado da operação é:', resultado)