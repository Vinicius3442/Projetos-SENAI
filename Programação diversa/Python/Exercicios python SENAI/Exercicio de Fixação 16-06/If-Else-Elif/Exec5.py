# Vinicius Montuani N° 29

ano = int(input("Digite um ano: "))


def anobissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True

resultado = anobissexto(ano)

if resultado:
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

