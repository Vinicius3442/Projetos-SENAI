def media_com_situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
    return media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_com_situacao(nota1, nota2, nota3)