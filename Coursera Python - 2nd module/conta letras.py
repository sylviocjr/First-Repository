'''
Jan 25, 2022
Strings extra homework 01 week 02 Coursera Python 2nd phase

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

def conta_letras(frase, contar = 'vogais'):
    
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    lista_consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 
                        'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    frase = frase.casefold()  # Transforma todas as letras em minúsculas.
    contador_letras = 0
    
    if contar == 'vogais':
        for cada_caractere in frase:
            i = 0
            while i < len(lista_vogais):
                if cada_caractere == lista_vogais[i]:
                    contador_letras += 1
                i += 1
    elif contar == 'consoantes':
        for cada_caractere in frase:
            i = 0
            while i < len(lista_consoantes):
                if cada_caractere == lista_consoantes[i]:
                    contador_letras += 1
                i += 1

    
    return contador_letras            
            


# print(conta_letras('programamos em python', 'consoantes'))