num = int(input("Digite um número para ver sua tabuada: "))
tabuada = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for calculo in tabuada:
    multiplicacao = num * calculo
    print(f"{num} X {calculo} = {multiplicacao}")