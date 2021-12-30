### 16 dez. 2021 ###
### Exercícios Coursera Semana 5 ###
### Função vogal(a) ###
### Deverá receber um parâmetro e retornar "True" se este for vogal. Do contrário, retornar "False" ###


def vogal(a):
    i = 0   
    lista = ['a','e','i','o','u','A','E','I','O','U']
    while i <= 9:
        if a == lista[i]:
            return True
            #break
            
        else:
            i+=1
            
    return False

letra = input('Digite a letra: ')
print(vogal(letra))
