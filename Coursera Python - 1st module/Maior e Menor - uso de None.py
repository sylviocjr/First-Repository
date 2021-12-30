### 09 dez. 2021 ###
### Exercício de obter o maior e menor número dentre os digitados ###
### Uso da atribuição "None" para inicializar uma variável ###
### Versão simplificada, sem validação das entradas ###

maior = menor = None

while True:
    numero = input("Digite um número inteiro qualquer ou 'fim' para sair: ")
    if numero == "fim":
        break
    else:
        numero = int(numero)
        
### Rotina importante para inicializar as variáveis "maior" e "menor", pois "None" não pode ser comparada com números. ###    
        if maior == None:
            maior = menor = numero   
### ------------------------------------------------------------------------------------------------------------------ ###
            
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print("Maior: ", maior)
print("Menor: ", menor)
    
    
