# Exercicio: Leia nome e verifique se a pessoa tem SILVA no nome
nome25 = input('Insira seu nome completo: ')
if nome25.find('Silva') >= 0:
    print('Este nome contém SILVA no sobrenome!')
else: 
    print('Este nome NÃO contém SILVA no sobrenome!')