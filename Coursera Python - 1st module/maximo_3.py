### 16 dez. 2021 ###
### Exercício 01 semana 5 Coursera ###
### Função maximo(a,b,c) ###
### Ao serem passados 3 parâmetros 'a' , 'b' e 'c' para a função, ela deverá retornar o maior dentre eles ###

def maximo(a,b,c):
    maior =  a 
    if b > a:
        maior = b
        if c > b:
            maior = c
    return(maior)

n1 = int(input('Digite o 1° n°: '))
n2 = int(input('Digite o 2° n°: '))
n3 = int(input('Digite o 3° n°: '))

print(maximo(n1,n2,n3))

            
