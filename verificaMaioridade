#Exercicio: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
nascimentos = []
maiores = []
menores = []
anoAtual =  date.today().year
for i in range(0, 7):
    nascimentos.append(int(input('Digite o {}º ano de nascimento. \n'.format(i + 1))))
for ano in nascimentos:
    if (anoAtual - ano) >= 18:
        maiores.append(ano)
    else:
        menores.append(ano)
print('{} pessoas já são de maiores.'.format(len(maiores)))
print('{} pessoas ainda são de menores.'.format(len(menores)))
