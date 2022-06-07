'''
Feb 27, 2022
Homework 01 week 6 Coursera Python 2nd phase.

For my own instructional purposes only.

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''
def soma_lista(lista):

    if len(lista) == 0:
        return 0
   
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])