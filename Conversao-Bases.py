#Exercicio 37: Ler um numero inteiro e converter para a base que o usuário escolher.
numero = int(input('Digite um número inteiro para ser convertido. \n'))
print('Número lido com sucesso. \nPara converter para: \n[1] Binário \n[2] Octal \n[3] Hexadecimal')
conversao = int(input('Digite sua opção:\n'))
while conversao < 1 or conversao > 3:
    conversao = int(input('Opção inválida, digite uma opção válida. \n'))
if conversao == 1:
    print('A forma binária do número {} é {}.'.format(numero, bin(numero)[2:]))
elif conversao == 2:
    print('A forma octal do número {} é {}.'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('A forma hexadecimal do número {} é {}.'.format(numero, hex(numero)[2:]))