'''
Jan 25, 2022
Strings homework 01 week 02 Coursera Python 2nd phase

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

def maiusculas(frase):
    frase = frase.replace(' ', '')

    string_doida = ''

    for cada_letra in frase:
        if ord(cada_letra) >= 65 and ord(cada_letra) <= 90:  # 65 dec = A; 90 dec = Z
            string_doida = string_doida + cada_letra
    return(string_doida)