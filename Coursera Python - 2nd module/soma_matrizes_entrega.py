'''
Jan 20, 2022
Matrices homework 02 week 01 Coursera Python 2nd phase
'''
### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

# Receber duas matrizes;
# Somar as duas matrizes;
# Caso não sejam de mesma dimensão, retornar False.

def soma_matrizes(m1, m2):
    if (len(m1) != len(m2)) or (len(m1[0]) != len(m2[0])):
        return False
    else:
        matriz_soma = []
        nr_linhas = len(m1)
        nr_colunas = len(m1[0])
        for i in range(nr_linhas):
            linhas = []
            for j in range(nr_colunas):
                linhas.append(m1[i][j] + m2[i][j])
            matriz_soma.append(linhas)
    return matriz_soma

# matriz_a = [[1, 1], [1, 1], [1,1]]
# matriz_b = [[2, 2], [2, 2], [2,2]]

# print("Soma das matrizes: ", soma_matrizes(matriz_a, matriz_b))