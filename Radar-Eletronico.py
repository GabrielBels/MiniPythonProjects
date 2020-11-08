#Exercicio: Leia a velocidade, se o carro ultrapassar 80km é multado R$7,00 por cada km acima do limite

velocidade = float(input('Qual a velocidade? \n'))
valor = 0
if velocidade > 80:
    valor = ((velocidade - 80) * 7)
    print('Você foi multado em R${:.2f}'.format(valor))
else: 
    print('Você não foi multado.')