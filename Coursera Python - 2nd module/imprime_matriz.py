'''
Jan 21, 2022
Matrices additional homework 01 week 01 Coursera Python 2nd phase '''

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

def imprime_matriz(matriz):
    
    i = 0

    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            print(matriz[i][j],"")
            j+=1
        print()  # Pula linha
        i+=1


imprime_matriz([[1],[2],[3]])
print()
imprime_matriz([[1,2,3],[4,5,6],[7,8,9]])
print()
imprime_matriz([[1,2,3]])
print() 
imprime_matriz([[1,2,3],[4,5,6]])
 
print("\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil\n")