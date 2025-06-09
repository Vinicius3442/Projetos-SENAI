produtos = []

for i in range(3):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    produtos.append((nome, preco))

mais_caro = produtos[0]
mais_barato = produtos[0]

for produto in produtos:
    if produto[1] > mais_caro[1]:
        mais_caro = produto
    if produto[1] < mais_barato[1]:
        mais_barato = produto

print(f"\nO produto mais caro é: {mais_caro[0]} com o preço de R${mais_caro[1]}")
print(f"O produto mais barato é: {mais_barato[0]} com o preço de R${mais_barato[1]}")
