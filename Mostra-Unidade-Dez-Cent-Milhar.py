# Exercicio: Ler numero de 0 a 9999 e mostrar separado UN DEZ CENT MILHAR ) 
numero = input('Digite um numero de 0 a 9999: ')
numerico = numero.isnumeric()
if numerico:
    if int(numero) >= 0 and int(numero) <= 9999: 
        if len(numero) == 4: print('Milhar | {} | \n Centena | {} | \n Dezena | {} | \n Unidade | {} |'.format(numero[0], numero[1], numero[2], numero[3]))
        elif len(numero) == 3: print('Centena | {} | \n Dezena | {} | \n Unidade | {} |'.format(numero[0], numero[1], numero[2]))
        elif len(numero) == 2: print('Dezena | {} | \n Unidade | {} |'.format(numero[0], numero[1]))
        elif len(numero) == 1: print('Unidade | {} |'.format(numero[0]))
    else: 
        print('O número digitado está fora do intervalo definido.')
        numero = ''
else: 
    print('Este não é um número.')