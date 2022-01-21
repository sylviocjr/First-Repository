'''
Jan 20, 2022
Matrices homework 02 week 01 Coursera Python 2nd phase
'''
### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

# Receber duas matrizes;
# Somar as duas matrizes;
# Caso não sejam de mesma dimensão, retornar False.

def soma_matrizes(matriz1, matriz2):
    if (len(matriz1) != len(matriz2)) or (len(matriz1[0]) != len(matriz2[0])):
        return False
    else:
        matriz_soma = []
        nr_linhas = len(matriz1)
        nr_colunas = len(matriz1[0])
        for i in range(nr_linhas):
            linhas = []
            for j in range(nr_colunas):
                linhas.append(matriz1[i][j] + matriz2[i][j])
            matriz_soma.append(linhas)
    return matriz_soma

matriz_a = [[1, 2, 3], [4, 5, 6]]
matriz_b = [[2, 3, 4], [5, 6, 7]]

print("\nSoma das matrizes: ", soma_matrizes(matriz_a, matriz_b))
print("\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil\n")