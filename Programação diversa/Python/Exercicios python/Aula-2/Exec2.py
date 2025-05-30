numInput = int(input("Insira um número: "))
numImpar = 1

while (numInput > numImpar):
    if numInput % 2 != 0:
        print(numImpar)
        numImpar += 2
        