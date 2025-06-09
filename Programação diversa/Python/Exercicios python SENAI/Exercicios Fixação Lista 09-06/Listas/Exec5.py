# Vinicius Montuani

produtos = {}

while True:
    nome = input("Nome do produto (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    preco = float(input("Preço do produto: "))
    produtos[nome] = preco


total = 0
print("\nProdutos comprados:")
for nome, preco in produtos.items():
    print(f"- {nome}: R${preco}")
    total += preco

print(f"\nTotal da compra: R${total}")
