#Exercicios: Faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no fim do jogo.
import random, time
def parImpar():
    ganhador = None
    ptsUser = 0
    while ganhador is None or ganhador == 'usuário':
        opcaoUser = input('Você quer PAR ou IMPAR?\n').lower()
        while opcaoUser != 'par' and opcaoUser != 'impar':
            opcaoUser = input('Valor inválido. PAR ou IMPAR?\n').lower()
        numUser = int(input('Digite um número de 0 a 10: \n'))
        while numUser < 0 or numUser > 10:
            numUser = int(input('Valor inválido. Digite um número ENTRE 0 e 10: \n'))
        opcaoPC = 'par' if opcaoUser == 'impar' else 'impar'
        numPc = int(random.randrange(0, 10))
        print(numPc, opcaoPC, (numUser + numPc) % 2)
        if opcaoUser == 'par' and ((numUser + numPc) % 2 == 0):
            ganhador = 'usuário'
            ptsUser += 1
            print('O usuário ganhou a rodada! \nUser {} x 0 PC'.format(ptsUser))
            time.sleep(2)
        elif opcaoUser == 'impar' and ((numUser + numPc) % 2 != 0):
            ganhador = 'usuário'
            ptsUser += 1
            print('O usuário ganhou a rodada! \nUser {} x 0 PC'.format(ptsUser))
            time.sleep(2)
        elif opcaoPC == 'impar' and ((numUser + numPc) % 2 != 0):
            print('O PC ganhou a rodada, fim de jogo.')
            ganhador = 'PC'
            time.sleep(2)
            break
        elif opcaoPC == 'par' and ((numUser + numPc) % 2 == 0):
            print('O PC ganhou a rodada, fim de jogo.')
            ganhador = 'PC'
            time.sleep(2)
            break
    if ptsUser > 1:
        print('Você ganhou {} vezes consecutivas.'.format(ptsUser))
        time.sleep(2)
        print('Parabéns!')
        time.sleep(2)
    elif ptsUser == 1 or ptsUser == 0:
        print('Que bosta, ganhou uma ou nenhuma vez. ')
        time.sleep(2)
        print('Boa sorte da próxima.')
        time.sleep(2)
parImpar()
