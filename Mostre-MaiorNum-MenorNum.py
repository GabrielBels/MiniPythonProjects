#Exercicio: Leia 3 numeros e mostre qual o maior e qual o menor
numeros = []
numeros.append(int(input('Digite primeiro numero: ')))
numeros.append(int(input('Digite segundo numero: ')))
numeros.append(int(input('Digite terceiro numero: ')))
numeros.sort()
print('O maior número foi {} e o menor foi {}'.format(numeros[len(numeros)-1],numeros[0]))