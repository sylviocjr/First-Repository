
### 10 dez. 2021 ###
### Exercício Coursera - comparar caracteres de uma string ###
### Comparar caracteres adjacentes e acusar caso haja, no mínimo, dois ...
### ... caracteres iguais. ###
### Posteriormente, fazer versão recomendada, considerando apenas inteiro numérico, empregando propriedades matemáticas. ###


numero = input('Digite um número inteiro: ')
tamanho = len(numero)
i = 0
adjacentes = False

while i < (tamanho-1):
    caractere = numero[i]
    #print(caractere)
    posterior = numero[i+1]
    #print(posterior)
    if caractere == posterior:
        adjacentes = True
    
    i += 1

if adjacentes == True:
    print('sim')
else:
    print('não')
    
    
