#Exercicio: Leia um número e responda se é par ou impar
numero30 = int(input('Digite um numero para saber se é par ou impar: '))
print('O numero {} é par'.format(numero30)) if numero30 % 2 == 0 else print('O numero {} é impar'.format(numero30))