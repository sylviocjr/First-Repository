'''
Feb 09, 2022
Homework 01 week 04 Coursera Python 2nd phase

For my own instructional purposes only.

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

def ordenada(lista):
    copia = lista[:]
    copia.sort()
    if lista == copia:
        return True
    return False

'''
lista = [3,2,1]
copia_lista = lista[:]
copia_lista.sort()
print("Lista não ordenada: ", lista)
print("\nLista ordenada: ", copia_lista)
print("\nResultado da função: ", ordenada(lista))
'''