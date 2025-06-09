valor_saque = int(input("Digite o valor a sacar (múltiplo de 10): "))

if valor_saque % 10 != 0:
    print("Valor inválido. Digite um múltiplo de 10.")
else:
    notas_50 = valor_saque / 50
    valor_restante = valor_saque % 50

    notas_20 = valor_restante / 20
    valor_restante %= 20

    notas_10 = valor_restante / 10

    print(f"Notas de R$50: {notas_50}")
    print(f"Notas de R$20: {notas_20}")
    print(f"Notas de R$10: {notas_10}")
