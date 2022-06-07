def encontra_impares(lista):

    lista_impares = []

    if len(lista) > 0:

        numero = lista.pop(0)

        if numero % 2 != 0:
            lista_impares.append(numero)

        lista_impares = lista_impares + encontra_impares(lista)

    return lista_impares