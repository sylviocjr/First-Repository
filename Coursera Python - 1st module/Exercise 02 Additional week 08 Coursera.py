### Jan. 5th, 2022 ###
### Exercise 02 Additional week 08 Coursera Python ###
### What does it do ??????  ###

### Key words: lists ###
### This script in Python creates a list from integers given by the user and, by means of a function, ... ###
### The flag to stop the list is 0, but 0 is not supposed to be shown in the final list (result) ###

### Palavras-chave: listas ###
### Este script em Python cria uma lista a partir de números inteiros fornecidos pelo usuário e reordena a lista em ordem invertida, imprimindo
### esta nova lista ao final ###
### A flag para interromper a lista é 0, mas 0 não pode ser exibido na lista final. Interessante a forma de eliminar o 0 da lista, caso
### o 0 seja inserido como uma sequência de 0 (00, 000 ...) e, dessa forma, não interpretado como o caractere '0' flag de saída ###

### Elaborar a versão para entrega: textos conforme template do exercício e eliminar itens não solicitados ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###



my_list = []


### Input Routine ###

while True:
    item = input("Enter an integer number to the list ('0' to exit): ")
    if item == "0":
        break
    else:
        try:
            item = int(item)
            my_list.append(item)
        except:
            continue

#my_list.sort()

if 0 in my_list:
    my_list.remove(0)   ### Removes 0 if 0 is input as a sequence of zeros (such as 00, 000 etc, thus not being understood as the flag to stop the list) ###

print("Here's your list: ", my_list)   ### Check !! ###

### End of input routine ###


### Action !!! ###

i = len(my_list) - 1
while i >= 0:
    print(my_list[i])
    i-=1

print ("\n\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")