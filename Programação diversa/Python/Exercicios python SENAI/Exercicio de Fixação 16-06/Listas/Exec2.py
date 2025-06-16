# Vinicius Montuani N° 29
idades = []
for i in range(4):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)
    
media_idades = sum(idades) / 4

print(f"Média das idades: {media_idades:.1f}")