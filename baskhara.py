
### 16 dez. 2021 ###
### Exercício proposto - Curso Python Coursera ###
### Dados os coeficientes de uma equação de segundo grau, mostrar as raízes e demais desdobramentos ###
### Exercício derivado da primeira versão, desta vez com uso de funções ###

import math

def delta(a,b,c):
    return b**2 - 4*a*c    ### Cálculo do DELTA ###
     
def raiz_1(a,b,d):   ### Parâmetro 'd' deverá receber o DELTA a ser repassado na chamada da função ###
    return (-b + math.sqrt(d))/(2*a) ### Observar o denominador entre parênteses, senão dá bug !!! Ver o vídeo da aula !!! ###

def raiz_2(a,b,d):   ### Parâmetro 'd' deverá receber o DELTA a ser repassado na chamada da função ###
    return (-b - math.sqrt(d))/(2*a) ### Observar o denominador entre parênteses, senão dá bug !!! Ver o vídeo da aula !!! ###

aa = bb = cc = 0

aa = float(input("Coeficiente a: "))
bb = float(input("Coeficiente b: "))
cc = float(input("Coeficiente c: "))

DELTA = delta(aa,bb,cc)

print("Delta = ", delta(aa,bb,cc))

if delta(aa,bb,cc) < 0:
    print("A equação não possui raízes em IR !")

elif delta(aa,bb,cc) == 0:

    print("A equação possui somente uma raiz real que é ", raiz_1(aa,bb,delta(aa,bb,cc)))
else:
    print("Raízes da equação: ", raiz_1(aa,bb,delta(aa,bb,cc)), "e", raiz_2(aa,bb,delta(aa,bb,cc)))
