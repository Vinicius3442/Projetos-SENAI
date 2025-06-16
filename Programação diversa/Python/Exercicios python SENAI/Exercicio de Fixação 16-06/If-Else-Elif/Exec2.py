# Vinicius Montuani N° 29

def mensagem_boas_vindas(nome):
    saudacao = f"Olá {nome}, seja bem-vindo(a)!"
    return saudacao


nome = input("Digite seu nome: ")

mensagem = mensagem_boas_vindas(nome)

print(mensagem)