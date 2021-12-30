### 16 dez. 2021 ###
### Exercícios Coursera Semana 5 ###
### Função vogal(a) ###
### Deverá receber um parâmetro e retornar "True" se este for vogal. Do contrário, retornar "False" ###


def vogal(a):
    i = 0   
    lista = ['a','e','i','o','u','A','E','I','O','U']
    for letra in lista:
        if a == lista[i]:
            return True
            #break    ### Parece não fazer sentido. O comando "return True" faz abandonar a função ??? ###
            
        else:
            i+=1
            
    return False   ### Retorna False caso nenhuma ocorrência seja encontrada ###

letra = input('Digite a letra: ')
print(vogal(letra))
