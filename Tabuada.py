#Exercicio: Mostre a tabuada de um número que o usuário escolher, só que agora utilizar o laço for.
numero = int(input('Digite um número para saber a tabuada:\n'))
for mult in range(1, 11):
  print('{} x {} = {}'.format(numero, mult, (numero * mult)))
