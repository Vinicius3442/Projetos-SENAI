def inverter_string(palavra):
    return palavra[::-1]

palavra = input("Digite uma palavra: ")
palavra_invertida = inverter_string(palavra)
print(f"A palavra {palavra} invertida é: {palavra_invertida}")


