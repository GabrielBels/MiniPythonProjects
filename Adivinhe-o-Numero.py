import random

#Exercicio: Computador escolhe um numero aleatorio entre 0 e 5 e o usuário tem que adivinhar
numPc = random.randrange(0, 5)
numUser = int(input('Qual numero você acha que o computador escolheu entre 0 e 5? \n'))
while numPc != numUser: 
        numUser = int(input('Errou, tente novamente. Digite outro numero: '))
print('Acertou, o numero escolhido pelo computador é {}!'.format(numPc))