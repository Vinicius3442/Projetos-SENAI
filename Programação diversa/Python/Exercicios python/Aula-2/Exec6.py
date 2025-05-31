numero = int(input("Digite um número inteiro positivo: "))
primo = 1
for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = 0
        break

if primo == 1:
    print(f"O {numero} é um número primo.")
else:
    print(f"O {numero} não é um número primo.")
