'''
Jan 28, 2022
Lists homework Hashtag Course - lists

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if 'livro' in produtos:
    # Encontrar índice do item 'livro' na lista de produtos:
    ind_livro = produtos.index('livro')
    #print("Indice de livro: ", ind_livro)

    # Armazenar para uso posterior o valor antigo de 'livro' na tabela antiga:
    preco_antigo = produtos_ecommerce[ind_livro][1]
    #print("Preço antigo livro: ", preco_antigo)

    # Alterar o valor do item 'livro' na lista de produtos_ecommerce em +10%:
    produtos_ecommerce[ind_livro][1] = int(produtos_ecommerce[ind_livro][1] * 1.1)
    print(produtos_ecommerce)

    # Cálculo do impacto financeiro:
    impacto_financeiro = produtos_ecommerce[ind_livro][0]*preco_antigo*0.10
    print("Impacto financeiro: R$", impacto_financeiro)

else:
    pass


print('\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.\n\n')