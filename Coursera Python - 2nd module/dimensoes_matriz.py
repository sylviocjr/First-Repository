'''
Jan 19, 2022
Matrices homework 01 week 01 Coursera Python 2nd phase
'''

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

def dimensoes(matriz):
    #print(matriz)
    #print(len(matriz))
    #print(len(matriz[0]))
    print(len(matriz),"X",len(matriz[0]))
    
minha_matriz = [[1, 2], [3, 4]]
dimensoes(minha_matriz)

minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)

minha_matriz = [[1,2,3],[4,5,6],[7,8,9]]
dimensoes(minha_matriz)

''' Obs: len(matriz) retorna número de linhas;
len(matriz[0]) retorna número de colunas. '''

