#Exercicio 36: Aprovar ou Reprovar um empréstimo bancário para compra de uma casa.
# O programa vai perguntar VLR DA CASA, o SALARIO do comprador, e PRAZO para pagamento.
# Calcule o valor da prestação mensal, sabendo que não poderá exceder 30% do salário ou então o empréstimo será negado.
# O valor dos juros usado foi de 0,85% a.m.
print('Seja bem-vindo ao nosso simulador bancário de empréstimo imobiliário.')
vlrCasa = float(input('Qual o valor da casa que deseja comprar? \n'))
salario = float(input('Certo.\n Qual o valor de seu salário atual? \n'))
prazo = int(input('Em quantos anos pretende pagar a casa? \n'))
prestacao = ((vlrCasa / (prazo * 12)) * 1.0085)
status = 'aprovado' if (salario * 0.3) > prestacao else 'reprovado'
print('Já colhemos as informações, e seu empréstimo foi {}.'.format(status))