'''
Jan 25, 2022
Strings homework 02 week 02 Coursera Python 2nd phase

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''


def menor_nome(nomes):
    lista_nova=[]
    for nome in nomes:
        lista_nova.append(nome.strip())
    
    mais_curto = lista_nova[0]  # Por default, mais curto é o primeiro nome da lista.
    for nome in lista_nova:
        if len(nome) < len(lista_nova[0]):
            mais_curto = nome
    mais_curto = mais_curto.capitalize()
    return(mais_curto)
