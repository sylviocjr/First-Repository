### Jan. 5th, 2022 ###
### Exercise 02 week 08 Coursera Python ###
### Sorting a list and deleting repeated elements from a list ###

### Key words: lists; functions ###
### This script in Python creates a list from integers given by the user and returns the sum of the numbers ###


### Palavras-chave: listas; funções ###
### Este script em Python cria uma lista a partir de números inteiros fornecidos pelo usuário e calcula a soma dos números ###

### Elaborar a versão para entrega: textos conforme template do exercício e eliminar itens não solicitados ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

def soma(lista_recebida):
    soma = i = 0
    while i <= len(lista_recebida)-1:
        soma = soma + lista_recebida[i]
        i+=1
    return soma

minha_lista = []


### Input Routine ###

while True:
    item = input("Enter an integer number to the list ('end' to exit): ")
    if item in ["end","End","END","ENd", "enD", "eND", "eNd", "EnD"]:
        break
    else:
        try:
            item = int(item)
            minha_lista.append(item)
        except:
            continue

minha_lista.sort()
print(minha_lista)   ### Check !! ###

### End of input routine ###


### Action !!! ###

somaLista = soma(minha_lista)
print("Soma dos números listados: ", somaLista)


print ("\n\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")
