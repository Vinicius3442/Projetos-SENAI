# Vinicius Montuani N°29

n = int(input("Digite um número para ver seus divisores: "))
divisores = []
for i in range(1, n+1):
    if n % i == 0:
        divisores.append(i)
print(f"Divisores de {n}: {divisores}")
if len(divisores) == 2:
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")