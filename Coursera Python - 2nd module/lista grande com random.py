'''
Feb 09, 2022
Additional Homework 01 week 04 Coursera Python 2nd phase

For my own instructional purposes only.

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

import random

def lista_grande(n):
    lista = []
    for i in range(n):
        numero = random.randint(0, 1000000)
        lista.append(numero)
    return(lista)
