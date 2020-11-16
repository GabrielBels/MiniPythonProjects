#Exercicio: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
def ehPalindromo(frase):
	reverse = frase.strip()[::-1]
	if (frase.lower() == reverse.lower()):
	    print('Esta frase é palíndroma.')
	else: 
	    print('Não é palíndroma.')

ehPalindromo(input('Digite uma frase: \n'))
