def calculo4 (num1, num2, num3, num4):
    soma = num1 + num2 + num3 + num4
    return soma

num1_Input = int(input(f"Digite o primeiro número: "))
num2_Input = int(input(f"Digite o primeiro número: "))
num3_Input = int(input(f"Digite o primeiro número: "))
num4_Input = int(input(f"Digite o primeiro número: "))

soma4 = calculo4(num1_Input, num2_Input, num3_Input, num4_Input)
print(f"A soma dos 4 números({num1_Input} + {num2_Input} + {num3_Input} + {num4_Input}) é igual a: {soma4}")