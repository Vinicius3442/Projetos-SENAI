# Vinicius Montuani N° 29

alunos = []

num_alunos = int(input("Quantos alunos deseja cadastrar? "))

for nomes in range(num_alunos):
    nome = input(f"Nome do aluno {nomes + 1}: ")
    nota = float(input(f"Nota do aluno {nomes + 1}: "))
    alunos.append({"nome": nome, "nota": nota})
    
media_turma = sum(aluno["nota"] for aluno in alunos) / len(alunos)
print(f"Média geral da turma: {media_turma:.1f}")
