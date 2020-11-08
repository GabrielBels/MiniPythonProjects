# Exercicio: Leia um nome e mostre o primeiro e o ultimo separadamente
nome27 = input('Digite seu nome completo: ')
separado27 = nome27.split()
print('O primeiro nome é {}'.format(separado27[0]))
print('O ultimo nome é {}'.format(separado27[len(separado27)- 1]))