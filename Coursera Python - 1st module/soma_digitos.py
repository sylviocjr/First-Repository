### 09 dez. 2021 ###
### Soma os dígitos de um número inteiro informado pelo usuário ###

soma_digitos = 0


soma_digitos = 0
numero = int(input("Digite um número inteiro: "))
if numero < 0:   ### Corrige para o caso de o número digitado ser negativo ###
    numero *=(-1)
                
while True:   
    unidade = numero % 10
    soma_digitos += unidade
    numero -= unidade
    numero /= 10
    if numero % 10 == 0 and numero < 10:   ### Segunda comparação evita Bug em caso de numeros que terminam com sequência de zeros ###
        break

print(int(soma_digitos))
   
