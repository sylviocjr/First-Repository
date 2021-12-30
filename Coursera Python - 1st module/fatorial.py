### 09 dez. 2021 ###
### Fatorial de um número ###

### Deverá ser digitado um número positivo inteiro que permita o cálculo ...
### ... de seu fatorial ###
### Por definição, assume 1 como fatorial natural de zero. ###

fatorial = aux = 1

numero = int(input("Digite o valor de n: "))

if numero != 0:
    
    while numero >= 1:
        aux = numero
        fatorial = fatorial * aux
        numero -=1   ### Decremento 1 unidade ###      

print(fatorial)
    
             
