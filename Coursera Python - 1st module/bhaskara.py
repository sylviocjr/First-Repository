
### 06 dez. 2021 ###
### Exercício Adicional proposto - Curso Python Coursera ###
### Dados os coeficientes de uma equação de segundo grau, mostrar as raízes e demais desdobramentos ###

import math

a = b = c = 0

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

delta = b**2 - 4*a*c

#print("Delta = ", delta)

if delta < 0:
    print("esta equação não possui raízes reais")

elif delta == 0:
    x = -b / 2*a
    print("a raiz desta equação é", x)
else:
    x1 = (-b + math.sqrt(delta))/(2*a)   ### Observar o denominador entre parênteses, senão dá bug !!! Ver o vídeo da aula !!! ###
    x2 = (-b - math.sqrt(delta))/(2*a)   ### Observar o denominador entre parênteses, senão dá bug !!! Ver o vídeo da aula !!! ###
    if x1 < x2:
        print("as raízes da equação são", x1, "e", x2)
    else:
        print("as raízes da equação são", x2, "e", x1)
