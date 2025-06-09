nomes = []
while True:
    nome = input("Digite um nome ou 'sair' para encerrar: ")
    if nome.lower() == "sair":
        break
    nomes.append(nome)

print("\nNomes digitados:")
for nome in nomes:
    print(nome)