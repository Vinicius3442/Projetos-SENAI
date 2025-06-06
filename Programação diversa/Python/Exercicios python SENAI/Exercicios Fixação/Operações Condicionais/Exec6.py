# Exercício 6: Vinicius Montuani 2°DEV B

selec = int(input("Selecione uma das opções: (1 - Saque, 2 - Depósito, 3 - Sair): "))

if selec == 1:
    print("Voce escolheu saque")
elif selec == 2:
    print("Voce escolheu depósito")
elif selec == 3:
    print("Voce escolheu sair")
else:
    print("Opção inválida")