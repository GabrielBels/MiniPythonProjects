#Exercicio: Faça um programa que leia um número inteiro e diga se ele é ou não um numero primo.
def ehPrimo(numero):
	divisores = []
	for i in range(1, numero + 1):
		if numero % i == 0:
			divisores.append(i)
	if len(divisores) == 2:
		print('Este é um número primo!')
	else:
		print('Este NÃO é um número primo!')

ehPrimo(int(input('Digite um numero: \n')))
