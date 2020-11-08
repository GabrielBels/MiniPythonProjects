#Exercicio 42: 
#1) Ler tamanho de 3 linhas e saber se podem formar um triangulo com base na condição de existencia de um triangulo;
#2) Mostrar qual tipo de triangulo será formado. 
#Exercicio 35 (Ler tamanho de 3 linhas e saber se podem formar um triangulo com base na condição de existencia de um triangulo)
linhaA = float(input('Digite o tamanho da primeira linha em cm: '))
linhaB = float(input('Digite o tamanho da segunda linha em cm: '))
linhaC = float(input('Digite o tamanho da terceira linha em cm: '))
if linhaA < (linhaB + linhaC) and linhaB < (linhaA + linhaC) and linhaC < (linhaA + linhaB):
    if linhaA == linhaB and linhaB == linhaC:
        print('Os valores {}, {} e {} formam um triângulo equilátero.'.format(linhaA, linhaB, linhaC))
    elif linhaA != linhaB and linhaB != linhaC:
        print('Os valores {}, {} e {} formam um triângulo escaleno.'.format(linhaA, linhaB, linhaC))
    elif (linhaA == linhaB and linhaA != linhaC) or (linhaA == linhaC and linhaA != linhaB) or (linhaB == linhaC and linhaB != linhaA):
        print('Os valores {}, {} e {} formam um triângulo isosceles.'.format(linhaA, linhaB, linhaC))
else:
    print('Os valores {}cm, {}cm e {}cm NÃO podem formar um triangulo.'.format(linhaA, linhaB, linhaC))
