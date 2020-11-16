#Exercicio: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. 
print('Mostrando todos numeros pares de 1 à 50:')
for num in range(1, 51):
  if num % 2 == 0:
    print(num)
