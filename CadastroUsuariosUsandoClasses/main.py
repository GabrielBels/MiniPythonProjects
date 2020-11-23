#Exercicio: 
#Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
#No final, mostre: A) qtas pessoas tem mais de 18 anos B) Quantos homens foram cadastrados. C) qtas mulheres tem menos de 20 anos 

from .classPessoa import Pessoa
  
def returnIdade(e):
  return e.idade
 
def returnMaisDezoito(e):
  return e.idade > 18
  
def inserirPessoa():
    opcao = 'Y'
    pessoas = []
    while(opcao.lower() == 'y'):
        pessoas.append(Pessoa((input('{}ª PESSOA: Digite o nome: \n'.format(len(pessoas) + 1))), (int(input('Digite a idade: \n'))), (input('H ou M?\n'))))
        opcao = input('Deseja inserir mais pessoas? (Se sim insira "Y", se não, insira "N")\n')
        while opcao.lower() != 'y' and opcao.lower() != 'n':
            opcao = input('OPÇÃO INVÁILDA! Se sim insira "Y", se não, insira "N".\n')    
    
    homens = []
    mulheresAteVinte = []
    maioresDezoito = []
   
    for i in range(0, len(pessoas)):
        if pessoas[i].sexo == 'H':
            homens.append(pessoas[i])
        elif pessoas[i].sexo == 'M':
            if pessoas[i].idade < 20:
                mulheresAteVinte.append(pessoas[i])
        if pessoas[i].idade > 18:
            maioresDezoito.append(pessoas[i])
                
    homens.sort(reverse=False, key=returnIdade)
    mulheresAteVinte.sort(reverse=False, key=returnIdade)
    maioresDezoito.sort(reverse=False, key=returnIdade)
    
    for i in range(0, len(homens)):
        print('{} {}| '.format(homens[i].nome, homens[i].idade), end="")
    print('\n')
    for i in range(0, len(mulheresAteVinte)):
        print('{} {} | '.format(mulheresAteVinte[i].nome, mulheresAteVinte[i].idade), end="")
    print('\n')
    for i in range(0, len(maioresDezoito)):
        print('{} {}| '.format(maioresDezoito[i].nome, maioresDezoito[i].idade), end="")
    
inserirPessoa()
