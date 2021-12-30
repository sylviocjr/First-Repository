### 18 dez. 2021 ###
### https://panda.ime.usp.br/aulasPython/static/aulasPython/aula06.html ###

### O número de combinações possíveis de m elementos em grupos de n elementos (n <= m) é dada pela fórmula de combinação m!/((m-n)!n!).
### Escreva um programa que lê dois inteiros m e n e calcula a combinação de m, n a n.



def funcao_fatorial(x):
    if x < 0:
        return 0
    fatorial = proximo = 1

    while proximo <= x:
        fatorial = fatorial * proximo
        proximo +=1

    return fatorial


n = m = 0

while n >= m:
    m = int(input('Digite o número de elementos m:'))
    n = int(input('Digite n:'))

print('Combinação de', m, 'elementos tomados', n, 'a', n, 'é:', int(funcao_fatorial(m)/(funcao_fatorial(m-n)*funcao_fatorial(n))))
    
    


