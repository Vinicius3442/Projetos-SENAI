# Vinicius Montuani N° 29

def media_situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
        
    return media, situacao

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = media_situacao(nota1, nota2, nota3)

print(f"O aluno foi/ficou {media[1]} com média {media[0]:.2f}.")
