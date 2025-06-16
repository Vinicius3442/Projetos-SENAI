saldo = 0
extrato = []
    
while True:
    opcao = input("1-Depositar \n2-Sacar \n3-Extrato\n4-Sair: ")
        
    if opcao == "1":
        valor = float(input("Valor do depósito: "))
        saldo += valor
        extrato.append(f"Depósito: +R${valor:.2f}")
            
    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        if valor <= saldo:
            saldo -= valor
            extrato.append(f"Saque: -R${valor:.2f}")
                
        else:
            print("Saldo insuficiente.")
            
    elif opcao == "3":
        print(f"Saldo atual: R${saldo:.2f}")
        
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")