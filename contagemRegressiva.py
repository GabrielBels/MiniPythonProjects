#Exercicio: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
print('Vamos começar a contagem regressiva para estourar os fogos...')
time.sleep(1)
for seg in range(10, 0, -1):
  print(seg)
  time.sleep(1)
  if seg == 1:
    print('ESTOURANDO FOGOS!!!!!!!!!!!')
