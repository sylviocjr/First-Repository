def elefantes(n):

    if n < 1:
        return ""  # Se n não for maior que 1, a função deve devolver uma string vazia.

    if n == 1:
        return "Um elefante incomoda muita gente\n"  # Observe que, para um elefante, você deve escrever por extenso e no singular ("Um elefante...").

    if n == 2:
        return "Um elefante incomoda muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais\n"
    else:
        return elefantes(n-1) + str(n-1) + " elefantes incomodam muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais\n"


def incomodam(n):
    
    if n < 1:
        return ""  # Se n não for maior que 1, a função deve devolver uma string vazia.

    else:
        return "incomodam " + incomodam(n-1)
