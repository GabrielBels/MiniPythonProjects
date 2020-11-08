import math, random

#Exercicio: Escolher aleatoriamente um aluno dos que foram digitados pelo usuário.
alunos = []
alunos.append(input('Aluno 1:'))
alunos.append(input('Aluno 2:'))
alunos.append(input('Aluno 3:'))
print('O aluno escolhido da vez foi {}'.format(random.choice(alunos)))