# Vinicius Montuani

alunos = {}

for i in range(3):
    nome = input(f"Digite o nome da {i+1} pessoa: ")
    nota = input(f"Digite a nota de {nome}: ")
    alunos[nome] = nota
    
escolha = int(input("Digite a opção\n 1) Aprovados 2) Reprovados:"))


if escolha == 1:
    for nome, nota in alunos.items():
        if float(nota) >= 7:
            print(f"{nome} está aprovado com a nota {nota}")
elif escolha == 2:
    for nome, nota in alunos.items():
        if float(nota) < 7:
            print(f"{nome} está reprovado com a nota {nota}")
else:
    print("Opção inválida")