# 03 dez. 2021
# Exercício 07 Capítulo 04


def computa_grau(x):
    if x >=0.9 and x <= 1.0:
        grau="A"
    elif x >=0.8 and x < 0.9:
        grau="B"
    elif x >=0.7 and x < 0.8:
        grau="C"
    elif x >=0.6 and x < 0.7:
        grau="D"
    elif x >=  0 and x < 0.6:
        grau="F"
    return grau

score=0
score=input("Digite uma nota:")

try:
    score=float(score)
    if score >= 0.0 and score <= 1.0:  #Esta verificação já remete à mensagem de erro caso a entrada numérica esteja fora dos limites !
        #print(score)
        conceito = computa_grau(score)
    print("Seu grau :",conceito)
except:
    print("Erro !!!")
