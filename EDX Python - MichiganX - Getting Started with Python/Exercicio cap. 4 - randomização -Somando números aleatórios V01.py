# 18 nov. 2021

# Randomização - cap. 4
# Objetivo: pedir ao usuário que informe um número inteiro dentro de certa faixa
# O programa deverá sortear 3 números que, somados, resultem no mesmo número
# informado pelo usuário.
# Será considerada inicialmente uma tabela de 0 a 10 como números possíveis
# de serem sorteados e somados.
# O usuário deverá informar o número de tentativas que deseja

import random # Fundamental !!!

numero=input("Informe um número positivo inteiro de 0 a 30:")
numero=int(numero)
tentativas = input("Quantas tentativas deseja :")
tentativas = int(tentativas)
controle = 0  # Designa uma variável que irá assinalar o caso de
# nenhuma combinação de números for encontrada, a fim de que
# se imprima uma única vez a mensagem de erro.

for i in range(tentativas):
    n1 = random.randint(0,10)
    n2 = random.randint(0,10)
    n3 = random.randint(0,10)
#    print(n1,n2,n3)
    if (numero == n1+n2+n3):
        print ("Os números somados foram", n1,n2,n3)
        controle = 1
if (controle == 0):
    print("Não foram encontrados números aleatórios !")
