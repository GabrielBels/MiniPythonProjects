import random

#Exercicio 28 (Computador escolhe um numero aleatorio entre 0 e 5 e o usuário tem que adivinhar)
numPc = random.randrange(0, 5)
print(numPc)
numUser = int(input('Qual numero você acha que o computador escolheu entre 0 e 5? \n'))
while numPc != numUser: 
        numUser = int(input('Errou, tente novamente. Digite outro numero: '))
print('Acertou, o numero escolhido pelo computador é {}!'.format(numPc))

#Exercicio 29 (Leia a velocidade, se o carro ultrapassar 80km é multado R$7,00 por cada km acima do limite)
velocidade = float(input('Qual a velocidade? \n'))
valor = 0
if velocidade > 80:
    valor = ((velocidade - 80) * 7)
    print('Você foi multado em R${:.2f}'.format(valor))
else: 
    print('Você não foi multado.')

#Exercicio 30 (Par ou impar?)
numero30 = int(input('Digite um numero para saber se é par ou impar: '))
print('O numero {} é par'.format(numero30)) if numero30 % 2 == 0 else print('O numero {} é impar'.format(numero30))

#Exercicio 31 (Leia a distancia de uma viagem, e calcule o preço da passagem. Até 200km R$ 0,50 por km | Mais que 200km R$0,45 por km)
distancia31 = float(input('Digite a distancia da viagem em quilometros: '))
valor = 0 
valor = distancia31 * 0.5 if distancia31 <= 200 else distancia31 * 0.45
print('O valor da passagem para uma viagem de {:.2f}km é de R$ {:.2f}'.format(distancia31, valor))

#Exercicio 32 (Leia o ano e informe se ele é bissexto)
ano32 = int(input('Digite o ano para saber se é bissexto: '))
bissexto = 'é' if (ano32 % 4 == 0) and (ano32 % 100 != 0) else 'não é'
print('O ano {} {} bissexto. '.format(ano32, bissexto))

#Exercicio 33 (Leia 3 numeros e mostre qual o maior e qual o menor)
numeros = []
numeros.append(int(input('Digite primeiro numero: ')))
numeros.append(int(input('Digite segundo numero: ')))
numeros.append(int(input('Digite terceiro numero: ')))
numeros.sort()
print('O maior número foi {} e o menor foi {}'.format(numeros[len(numeros)-1],numeros[0]))

#Exercicio 34 (Leia o salario do funcionario e calcule o aumento. Se for ate 1250 o aumento é de 10% se for maior que 1250 15%)
salario = float(input('Digite o valor do seu salario: '))
aumento = 0.1 if salario <= 1250 else 0.15
print('Seu salario de R${:.2f} foi aumentado para R${:.2f}'.format(salario, (salario * (1 + aumento))))

#Exercicio 35 (Ler tamanho de 3 linhas e saber se podem formar um triangulo com base na condição de existencia de um triangulo)
linhaA = float(input('Digite o tamanho da primeira linha em cm: '))
linhaB = float(input('Digite o tamanho da segunda linha em cm: '))
linhaC = float(input('Digite o tamanho da terceira linha em cm: '))
if linhaA < (linhaB + linhaC) and linhaB < (linhaA + linhaC) and linhaC < (linhaA + linhaB):
    print('Os valores {}, {} e {} podem formar um triangulo SIM.'.format(linhaA, linhaB, linhaC))
else:
    print('Os valores {}cm, {}cm e {}cm não podem formar um triangulo NÃO.'.format(linhaA, linhaB, linhaC))