#Exercicio: Ler tamanho de 3 linhas e saber se podem formar um triangulo com base na condição de existencia de um triangulo
linhaA = float(input('Digite o tamanho da primeira linha em cm: '))
linhaB = float(input('Digite o tamanho da segunda linha em cm: '))
linhaC = float(input('Digite o tamanho da terceira linha em cm: '))
if linhaA < (linhaB + linhaC) and linhaB < (linhaA + linhaC) and linhaC < (linhaA + linhaB):
    print('Os valores {}, {} e {} podem formar um triangulo SIM.'.format(linhaA, linhaB, linhaC))
else:
    print('Os valores {}cm, {}cm e {}cm não podem formar um triangulo NÃO.'.format(linhaA, linhaB, linhaC))