#Exercicio: Leia o ano e informe se ele é bissexto
ano32 = int(input('Digite o ano para saber se é bissexto: '))
bissexto = 'é' if (ano32 % 4 == 0) and (ano32 % 100 != 0) else 'não é'
print('O ano {} {} bissexto. '.format(ano32, bissexto))