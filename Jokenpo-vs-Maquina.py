#JOGUE JOKENPÔ CONTRA SEU PROPRIO COMPUTADOR
import random, time
sinal = ['Pedra', 'Papel', 'Tesoura']
vitoriaPc = 0
vitoriaUser = 0
rodada = 0
while vitoriaPc < 3 and vitoriaUser < 3:
    sinalPc = random.choice(sinal)
    if rodada == 0:
        print('Seja bem-vindo ao JOKENPÔ.')
        time.sleep(1)
        print('Quem fizer 3 pontos primeiro ganha a partida.')
        time.sleep(2)
        print('Começando o jogo...')
        time.sleep(1)
    else: 
        time.sleep(1)
        print('\033[1;30;43mPLACAR MÁQUINA {} X {} USER\033[0;0m'.format(vitoriaPc, vitoriaUser))
    print('---------\nPEDRA\nPAPEL\nTESOURA\n---------\nDigite qual você quer?')
    sinalUser = input('').capitalize()
    time.sleep(1)
    if (sinalPc == 'Pedra' and sinalUser == 'Papel') or (sinalPc == 'Papel' and sinalUser == 'Tesoura') or (sinalPc == 'Tesoura' and sinalUser == 'Pedra'):
        vitoriaUser = vitoriaUser + 1
        rodada = rodada + 1 
        time.sleep(1)
        print('A máquina escolheu {}.'.format(sinalPc)) 
        time.sleep(1)
        print('\033[1;32;1mVitória para o usuário!\033[0;0m\n')
        time.sleep(2)
    elif (sinalPc == 'Pedra' and sinalUser == 'Tesoura') or (sinalPc == 'Papel' and sinalUser == 'Pedra') or (sinalPc == 'Tesoura' and sinalUser == 'Papel'):
        rodada = rodada + 1 
        vitoriaPc = vitoriaPc + 1
        time.sleep(1)
        print('A máquina escolheu {}.'.format(sinalPc))
        time.sleep(1)
        print('\033[1;31;1mVitória para a máquina.\033[0;0m\n')
        time.sleep(2)
    elif (sinalPc == 'Pedra' and sinalUser == 'Pedra') or (sinalPc == 'Papel' and sinalUser == 'Papel') or (sinalPc == 'Tesoura' and sinalUser == 'Tesoura'):
        rodada = rodada + 1 
        time.sleep(1)
        print('A máquina também escolheu {}.'.format(sinalPc))
        time.sleep(1)
        print('Empate.\n')
        time.sleep(2)
    else:
        print('Opção inválida. :(\n')
        rodada = rodada + 1 
if vitoriaPc == 3:
    print('\033[1;31;1mQue pena, a máquina ganhou! :(\033[0;0m')
elif vitoriaUser == 3:
    print('\033[1;32;1mPARABÉNS, VOCÊ GANHOU! :)\033[0;0m')
