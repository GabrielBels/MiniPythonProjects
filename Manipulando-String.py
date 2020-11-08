# Exercicio: Ler nome e mostrar:
# 1) TODAS LETRAS MAIUSCULAS 2) TODAS MINUSCULAS 3) CONTAR LETRAS *SEM ESPAÇOS* 4) QUANTAS LETRAS TEM A PRIMEIRA PALAVRA
nome = input('Digite o seu nome: ')
nomeSeparado = nome.split()
print('Todas letras maiusculas: {}'.format(nome.upper()))
print('Todas letras maiusculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(''.join(nomeSeparado))))
print('Quantidade de letras da primeira palavra: {}'.format(len(nomeSeparado[0])))