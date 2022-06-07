'''
Feb 24, 2022
Binary Search program - Function Binary Search

For my own instructional purposes only.

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista)-1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) //2
        print(meio)
        if lista[meio] == elemento:
            return meio
        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1

    return False
