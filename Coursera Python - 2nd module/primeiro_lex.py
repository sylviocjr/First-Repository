'''
Jan 26, 2022
Strings extra homework 02 week 02 Coursera Python 2nd phase

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

def primeiro_lex(lista):
    primeiro = lista[0]  # Por Default
    
    for cada_string in lista:
        if cada_string < primeiro:
            primeiro = cada_string

    return primeiro

'''
Testes:
print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
print(primeiro_lex(['AAAAAA', 'b']))
print(primeiro_lex(['joão', 'josé', 'maria', 'blumenau']))
'''