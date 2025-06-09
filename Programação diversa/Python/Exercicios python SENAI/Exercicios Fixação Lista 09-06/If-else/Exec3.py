altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc}")

if imc < 18.5:
    print("Classificação: Baixo peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Classificação: Obesidade grau 1")
elif 35 <= imc < 39.9:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3")