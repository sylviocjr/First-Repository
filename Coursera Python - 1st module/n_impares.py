### 09 dez. 2021 ###
### Imprime n primeiros números ímpares naturais ###
### O usuário deverá informar 'n', ou seja, quantos números ímpares ...
### ... deverão ser gerados. ###

impar = 1 ### Define o primeiro númeor ímpar para iniciar a contagem ###
cont = 1

n = int(input("Digite o valor de n: "))

if n > 0:

    while cont <= n:
        print (impar)
        impar += 2   # incremento em 2 unidades ###
        cont += 1    # incrementa o contador em 1 unidade ###
