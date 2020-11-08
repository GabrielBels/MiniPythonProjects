import math, random

#Exercicio: Ler alunos e sortear ordem de apresentação de trabalho
alu = []
alu.append(input('Aluno 1:'))
alu.append(input('Aluno 2:'))
alu.append(input('Aluno 3:'))
alu.append(input('Aluno 4:'))
print(random.sample(alu, len(alu)))