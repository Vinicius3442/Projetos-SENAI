# Exercício 5: Vinicius Montuani 2°DEV B

def listaNomes(nomes):
    for nome in nomes:
        print(f"Nome: {nome}")

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")

nomes = [nome1, nome2, nome3]

listaNomes(nomes)