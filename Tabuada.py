### 08 dez. 2021 ###
### Exercícios de estrutura de repetição e concatenação ###
### Programa Tabuada ###
### Observar a atribuição dada ao incremento dentro do loop ###

tabuada_de = int(input('Digite o número inteiro da tabuada: '))
multiplicador = 1 ### Elemento neutro para multiplicação ###

while multiplicador <= 10:
    print(tabuada_de, " x ", multiplicador, " = ", tabuada_de*multiplicador)
    multiplicador +=1   ### Observar esta forma de incrementar ###

print("Fim da tabuada de", tabuada_de)
