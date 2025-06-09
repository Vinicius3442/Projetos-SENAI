def cria_Conta(nome, conta_numero, saldo, limite):
    conta = {"nome" :nome, "c/c": conta_numero, "saldo":saldo, "limite":limite}
    return conta

def depositar(conta, valor):
    conta['saldo'] += valor
    print(f"Voce depositou R${valor},00 e agora obtem R${conta['saldo']:.2f} de saldo")
    return conta

def sacar(conta, valor):
    conta['saldo'] -= valor
    print(f"Voce sacou R${valor},00 e ainda possui R${conta['saldo']},00 de saldo")
    return conta

def extrato(conta):
    print(f"Saldo atual: R${conta['saldo']:.2f}")

nome = input("Digite seu nome: ")
conta_numero = input("Digite sua conta: ")
saldo = int(input("Digite seu saldo: "))
limite = 10000

conta = cria_Conta(nome, conta_numero, saldo, limite)

escolha = input("\nEscolha uma operação \n1) Sacar\n2) Depositar\n3) Extrato\n")

if escolha == "1":
    valor = int(input("Digite o valor a ser sacado: "))
    conta = sacar(conta, valor)

elif escolha == "2":
    valor = int(input("Digite o valor a ser depositar"))
    conta = depositar(conta, valor)

elif escolha == "3":
    extrato(conta)

else:
    print("Opção inválida, tente novamente")