numeros = [i for i in range(1, 101)]
soma = 0

for par in numeros:
    if par % 2 == 0:
        soma += par
print(f"A soma de todos os números pares é: {soma}")