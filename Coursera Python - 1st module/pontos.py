###07 dez. 2021 ###
### Exercício 02 Adicional semana 3 - Distância entre pontos no R2 ###
### Incrementado com o uso de funções ###

import math

#------------ Função para calcular a distância -----------#
def calcula_distancia(a,b,c,d):
    return math.sqrt(((a-b)**2)+((c-d)**2))
#---------------------------------------------------------#    


x1 = int(input('Abscissa do primeiro ponto: '))
y1 = int(input('Ordenada do primeiro ponto: '))

x2 = int(input('Abscissa do segundo ponto: '))
y2 = int(input('Ordenada do segundo ponto: '))

distancia = calcula_distancia(x1,x2,y1,y2)
#print('Distância: ',distancia)

if distancia >= 10:
    print('longe')
else:
    print('perto')
