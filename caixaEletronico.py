# Exercicio: 
# Crie um programa que simule o funcionamento de um caixa eletronico. 
# No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# (CONSIDERE CEDULAS DE 50, 20, 10 e 1)

import time
def caixaEletronico(valor):

    cinquenta = 0
    vinte = 0
    dez = 0
    um = 0
    
    while (valor > 10000):
        valor = int(input('O limite de saque diário é de R$ 10.000,00.\nInsira o valor novamente.\n'))
    
    while (valor >= 50):
        cinquenta += 1
        valor -= 50
    while (valor >= 20):
        vinte += 1
        valor -= 20
    while (valor >= 10):
        dez += 1 
        valor -= 10
    while (valor >= 1):
        um += 1
        valor -= 1
    
    print('\nVOCÊ RECEBERÁ:')
    if cinquenta > 0:
        print('{} cédulas de R$ 50,00'.format(cinquenta))
    if vinte > 0:
        print('{} cédulas de R$ 20,00'.format(vinte))
    if dez > 0:
        print('{} cédulas de R$ 10,00'.format(dez))
    if um > 0:
        print('{} cédulas de R$ 1,00'.format(um), end="")
        
caixaEletronico(int(input('Digite o valor a ser sacado:\n')))
