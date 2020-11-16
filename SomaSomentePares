#Exercicio: Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
acumulador = 0
valores = []
for value in range(0, 6):
	valores.append(int(input('Digite o {}º valor: '.format(value+1))))
for parImpar in valores:
	if parImpar % 2 == 0: 
		print('{} + {} = {}'.format(acumulador, parImpar, (acumulador + parImpar)))
		acumulador = acumulador + parImpar
print('Valor final da soma dos numeros pares: {}'.format(acumulador)) 
