# Exercício 3: Vinicius Montuani 2°DEV B

def par_impar(num):
    
    if num % 2 == 0:
        return "Par"
    
    else:
        return "Ímpar"
    
num = int(input("Digite um número: "))

resultado = par_impar(num)

print(f"O número {num} é {resultado}.")