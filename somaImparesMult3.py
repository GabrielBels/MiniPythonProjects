#Exercicio: Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de tres e se encontram no intervalo de 1 ate 500.
acumulador = 0
for num in range(1, 501):
  if num % 3 == 0:
    print('{} + {} = {}'.format(acumulador, num, (acumulador + num)))
    acumulador = acumulador + num
