### 16 dez. 2021 ###
### Exercício 01 semana 5 Coursera ###
### Função maximo(a,b) ###
### Ao serem passados dois parâmetros 'a' e 'b' para a função, ela deverá retornar o maior dentre eles ###

def maximo(a,b):
    maior =  a 
    if b > a:
        maior = b
    return(maior)

n1 = int(input('Digite o 1° n°: '))
n2 = int(input('Digite o 2° n°: '))

print(maximo(n1,n2))

            
