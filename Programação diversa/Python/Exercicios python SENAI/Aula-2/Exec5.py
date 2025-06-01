numInput = int(input("Digite um número: "))

numeros = [i for i in range(1, numInput + 1)]
soma = 0

for par in numeros:
    if par % 2 == 0:
        soma += par
print(f"A soma de todos os números pares do 1 até {numInput} é: {soma}")