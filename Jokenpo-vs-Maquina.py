#Exercicio 45: Faça um programa onde o computador joga Jokenpô com você
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
        print('PLACAR MÁQUINA {} X {} USER.'.format(vitoriaPc, vitoriaUser))
    print('---------\nPEDRA\nPAPEL\nTESOURA\n---------\nDigite qual você quer?')
    sinalUser = input('').capitalize()
    time.sleep(1)
    if (sinalPc == 'Pedra' and sinalUser == 'Papel') or (sinalPc == 'Papel' and sinalUser == 'Tesoura') or (sinalPc == 'Tesoura' and sinalUser == 'Pedra'):
        vitoriaUser = vitoriaUser + 1
        rodada = rodada + 1 
        time.sleep(1)
        print('A máquina escolheu {}.'.format(sinalPc)) 
        time.sleep(1)
        print('Vitória para o usuário.\n')
        time.sleep(2)
    elif (sinalPc == 'Pedra' and sinalUser == 'Tesoura') or (sinalPc == 'Papel' and sinalUser == 'Pedra') or (sinalPc == 'Tesoura' and sinalUser == 'Papel'):
        rodada = rodada + 1 
        vitoriaPc = vitoriaPc + 1
        time.sleep(1)
        print('A máquina escolheu {}.'.format(sinalPc))
        time.sleep(1)
        print('Vitória para a máquina.\n')
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
if vitoriaPc == 3:
    print('Que pena, a máquina ganhou! :(')
elif vitoriaUser == 3:
    print('PARABÉNS, VOCÊ GANHOU! :)')