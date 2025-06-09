frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador_vogais = 0

for letra in frase:
    if letra in vogais:
        contador_vogais += 1

print("A frase tem", contador_vogais, "vogais.")
