def palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        print(f"A palavra {palavra} é um palíndromo.")
    else:
        print(f"A palavra {palavra} não é um palíndromo.")

palavra = input("Digite uma palavra: ")
palindromo(palavra)

