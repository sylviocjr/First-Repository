### 18 dez. 2021 ###
### Função Fatorial de um número ###

### Deverá ser digitado um número positivo inteiro que permita o cálculo de seu fatorial ###


def funcao_fatorial(n):
    if n < 0:
        return 0
    fatorial = proximo = 1

    while proximo <= n:
        fatorial = fatorial * proximo
        proximo +=1

    return fatorial


numero = int(input("Digite o valor de n: "))   

print('Fatorial de', numero, 'é:', funcao_fatorial((numero)))
