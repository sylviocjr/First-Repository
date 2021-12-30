### 18 dez. 2021 ###
### Fatorial de um número - Versão aprimorada - começa do zero (0) e incrementa os valores ###

### Deverá ser digitado um número positivo inteiro que permita o cálculo ...
### ... de seu fatorial ###

fatorial = proximo = 1
numero = -1

while numero < 0:
    numero = int(input("Digite um número inteiro positivo: "))

  
while proximo <= numero:
    fatorial = fatorial * proximo
    proximo +=1       

print('Fatorial de', numero, 'é:', fatorial)
    
             
