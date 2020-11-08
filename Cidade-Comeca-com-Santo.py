# Exercicio: Ler nome da cidade e verificar se começa com SANTO
cidade = input('Digite o nome da cidade: ')
if cidade[:5].lower() == 'santo':
    print('A cidade {} começa com SANTO sim!'.format(cidade))
else: 
    print('A cidade {} NÃO começa com SANTO!'.format(cidade))