### 16 dez. 2021 ###
### Exercícios Coursera Semana 5 ###
### Função vogal(a) ###
### Deverá receber um parâmetro e retornar "True" se este for vogal. Do contrário, retornar "False" ###


def vogal(a):
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U':
        return True
    else:
        return False

letra = input('Digite a letra: ')
print(vogal(letra))
