def nome_mais_curto(lista):
    lista_nova=[]
    for nome in lista:
        lista_nova.append(nome.strip())
    
    mais_curto = lista_nova[0]  # Por default, mais curto é o primeiro nome da lista.
    for nome in lista_nova:
        if len(nome) < len(lista_nova[0]):
            mais_curto = nome
    mais_curto = mais_curto.capitalize()
    return(mais_curto)


lista = ["   ana   ", "banana", "bozo  ", "sabiá"]


print("Nome mais curto:", nome_mais_curto(lista))