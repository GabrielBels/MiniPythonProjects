#Exercicio 39: Leia o ano de nascimento de um jovem e dê informaçoes do tempo para se alistar ao serviço militar
from datetime import date
nascimento = int(input('Digite o seu ano de nascimento. \n'))
anoAtual =  date.today().year
if anoAtual - nascimento == 18:
    print('Você deve se alistar neste ano.')
elif anoAtual - nascimento < 18:
    print('Você deverá se alistar daqui a {} anos.'.format(18 - (anoAtual - nascimento)))
elif anoAtual - nascimento > 18: 
    print('Você deveria ter se alistado há {} anos.'.format((anoAtual - nascimento) - 18))