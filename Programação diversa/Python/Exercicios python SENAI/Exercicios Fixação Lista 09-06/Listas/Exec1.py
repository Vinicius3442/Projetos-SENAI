# Vinicius Montuani

agenda = {}

for i in range(3):
    nome = input(f"Digite o nome da {i+1} pessoa: ")
    telefone = input(f"Digite o telefone de {nome}: ")
    agenda[nome] = telefone.lower()


while True:
    buscar = input("Digite o nome para buscar o telefone (ou digite lista para mostrar os nomes): ")
    if buscar in agenda:
        print(f"O telefone de {buscar} é: {agenda[buscar]}")
    elif buscar == "lista":
        print(agenda)

    else:
        print(f"{buscar} não encontrado na agenda.")
