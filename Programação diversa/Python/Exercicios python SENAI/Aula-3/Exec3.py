import tkinter as tk
from tkinter import messagebox

# Versão original (console_app) do código comentado:
# def criaçãoPersonagem (nome, email, raca, idade, sexo, server):
#     print("Confira as informaçãos do personagem:\n")
#     print(f"{nome}\t{email}\t{raca}\t{idade}\t{sexo}\t{server}")
#     print("O personagem foi criado com sucesso")
    
# nome = input("Digite o nome do seu personagem: ")
# email = input("Digite o email do seu personagem: ")
# raca = input("Digite a raça do seu personagem: ")
# idade = input("Digite a senha do seu personagem: ")
# sexo = input("Digite o sexo do seu personagem (M ou F): ")
# server = input("Digite o server do seu personagem (S1, S2, S3): ")

# validacao = criaçãoPersonagem(nome, email, raca, idade, sexo, server)

def criar_personagem():
    nome = entry_nome.get()
    email = entry_email.get()
    raca = entry_raca.get()
    idade = entry_idade.get()
    sexo = entry_sexo.get()
    server = entry_server.get()
    resultado = (
        f"Confira as informações do personagem:\n"
        f"Nome: {nome}\n"
        f"Email: {email}\n"
        f"Raça: {raca}\n"
        f"Idade: {idade}\n"
        f"Sexo: {sexo}\n"
        f"Server: {server}\n"
        "O personagem foi criado com sucesso!"
    )
    messagebox.showinfo("Personagem Criado", resultado)
# Criação da janela principal
root = tk.Tk()
root.title("Criação de Personagem")
root.geometry("400x300")
root.configure(bg="#288062")

# Criação dos campos de entrada:
label = tk.Label(root, text="Preencha os dados do personagem:", bg="#285880", width=400, height=10, fg="#ffffff")
label.pack()
# Nome
label_nome = tk.Label(root, text="Nome:", fg="#ffffff")
label_nome.pack(pady=5)
label_nome.configure(bg="#288062" )
entry_nome = tk.Entry(root)
entry_nome.pack()
entry_nome.configure(bg="#ffffff", fg="#000000")

# Email
label_email = tk.Label(root, text="Email:", fg="#ffffff")
label_email.pack(pady=5)
label_email.configure(bg="#288062")
entry_email = tk.Entry(root)
entry_email.pack()

# Raça
label_raca = tk.Label(root, text="Raça:", fg="#ffffff")
label_raca.pack(pady=5)
label_raca.configure(bg="#288062")
entry_raca = tk.Entry(root)
entry_raca.pack()

# Idade
label_idade = tk.Label(root, text="Idade:", fg="#ffffff")
label_idade.pack(pady=5)
label_idade.configure(bg="#288062")
entry_idade = tk.Entry(root)
entry_idade.pack()

# Sexo
label_sexo = tk.Label(root, text="Sexo (M ou F):", fg="#ffffff")
label_sexo.pack(pady=5)
label_sexo.configure(bg="#288062")
entry_sexo = tk.Entry(root)
entry_sexo.pack()

# Server
label_server = tk.Label(root, text="Server (S1, S2, S3):", fg="#ffffff")
label_server.pack(pady=5)
label_server.configure(bg="#288062")
entry_server = tk.Entry(root)
entry_server.pack()

# Criação do botão para criar o personagem
botao_criar = tk.Button(root, text="Criar Personagem", command=criar_personagem)
botao_criar.pack(pady=25)
botao_criar.configure(bg="#285880", fg="#ffffff", width=20, height=2)
# Inicia o loop principal da interface gráfica
root.mainloop()