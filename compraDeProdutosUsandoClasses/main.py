from .classProduto import Produto
 
def returnPreco(e):
  return e.preco
  
def inserirProduto():
    opcao = 'Y'
    produtos = []
    acimaMil = []
    total = 0
    
    while(opcao.lower() == 'y'):
        produtos.append(Produto(input('{}ª PRODUTO: Digite o nome: \n'.format(len(produtos) + 1)), float(input('Digite o preco: \n'))))
        opcao = input('Deseja inserir mais produtos? (Se sim insira "Y", se não, insira "N")\n')
        while opcao.lower() != 'y' and opcao.lower() != 'n':
            opcao = input('OPÇÃO INVÁILDA! Se sim insira "Y", se não, insira "N".\n')    
    
    for i in range(0, len(produtos)):
       total += produtos[i].preco
       if produtos[i].preco > 1000:
            acimaMil.append(produtos[i])
        
           
    produtos.sort(reverse=False, key=returnPreco)

    print('A) Foi gasto na compra o total de R${}'.format(total))
    if acimaMil:
        print('B)| ', end="")
        for i in range(0, len(acimaMil)):
            print('{} {} | '.format(acimaMil[i].nome, acimaMil[i].preco), end="")
    else:
        print('B) Não há produtos acima de mil reais.')
    print('\nC) O produto mais barato é {}'.format(produtos[0].nome))
    
inserirProduto()
