


def imprime_retangulo(a,b):

    cont = 1
    while cont <= b:
        imprime_largura(a)
        print()
        cont+=1
    

def imprime_largura(a):

    cont1 = 1
    while cont1 <= a:
        print("", end = "")
        cont1+=1

largura = 120
altura = 35

imprime_retangulo(largura,altura)
