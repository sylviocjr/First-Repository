'''
Jan 19, 2022
Programa introdutório a matrizes - entender a manipulação dos índices
'''
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print('\n',matriz,'\n')

i = 0

while i <= 2:
    j = 0
    while j <= 2:
        print(matriz[i][j], end = ' ')
        j+=1
    print()  # Pula linha
    i+=1
print('\n')
i = 0
while i <= 2:
    print(matriz[i], end='\n')  # Indexado apenas pelo índice de linha !!
    i+=1
print('\n')