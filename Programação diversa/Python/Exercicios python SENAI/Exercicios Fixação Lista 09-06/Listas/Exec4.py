# Vinicius Montuani


# Não consegui fazer com dicionario :(
tarefas = []

while True:
    acao = input("Digite 'add' para adicionar, 'remover' para remover: ")

    if acao == "add":
        nome = input("Nome da tarefa a ser adicionada: ")
        tarefas.append(nome)
        print("Tarefa adicionada.")

    elif acao == "remover":
        nome = input("Nome da tarefa para ser removida: ")
        if nome in tarefas:
            tarefas.remove(nome)
            print("Tarefa removida.")
        else:
            print("Tarefa não encontrada.")

    print("Lista de tarefas:")
    for nomes in tarefas:
        print("-", nomes)
