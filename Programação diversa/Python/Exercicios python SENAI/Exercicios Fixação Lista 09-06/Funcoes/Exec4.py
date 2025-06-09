def maior_numero_lista(lista):
    return max(lista)


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

lista = [num1, num2, num3]

maior = maior_numero_lista(lista)

print("O maior número é o:", maior)