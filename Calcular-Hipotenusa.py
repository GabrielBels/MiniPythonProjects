import math

# Exercicio: Calcular hipotenusa com base nos catetos
catOposto = float(input('Insira o comprimento em cm do cateto oposto: '))
catAdjas = float(input('Insira o comprimento em cm do cateto adjacente: '))
hipotenusa = math.hypot(catOposto, catAdjas)
print('O comprimento da hipotenusa é: {} cm'.format(hipotenusa))
