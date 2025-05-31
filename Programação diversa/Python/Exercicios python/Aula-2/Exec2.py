x = int(input("Insira um número: "))
soma = 0
impares = 1
while impares <= x:
    soma += impares
    impares += 2
print(f"A soma de todos os números impares de 1 até {x} é: {soma}")