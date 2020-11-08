import math

# Exercicio: Mostrando SEN, COS, TAN com base no ângulo
angulo = int(input('Insira o valor do angulo para saber o seno, cosseno e tangente: '))
seno = int(math.sin(math.radians(angulo)))
cosseno = int(math.cos(math.radians(angulo)))
tangente = math.tan(math.radians(angulo))
print('Angulo: {} |-> Seno: {}, Cosseno: {}, Tangente: {}'.format(angulo, seno, cosseno, tangente))