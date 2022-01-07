### Jan. 4th, 2022 ###
### Exercise 01 week 08 Coursera Python ###
### Sorting a list and deleting repeated elements from a list ###

### Key words: lists; functions ###
### This script in Python creates a list from integers given by the user, deletes repeated elements from this list and sorts the elements ###
### At the end, it shows a new list containing only single elements ###

### Palavras-chave: listas; funções ###
### Este script em Python cria uma lista a partir de números inteiros fornecidos pelo usuário, elimina os valores repetidos e ordena a lista ###
### Ao final, mostra a nova lista apenas com os elementos sendo exibidos uma única vez ###

### Elaborar a versão para entrega: textos conforme template do exercício e eliminar itens não solicitados ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###


def del_repeated(list):
    i = 0
    while i <= len(list)-2:
        j = 1
        while j <= len(list)-1:
            if list[i] == list[j] and i != j:
                del list[j]
            j+=1
        i+=1
    return(list)


my_list = []


### Input Routine ###

while True:
    item = input("Enter an integer number to the list ('end' to exit): ")
    if item in ["end","End","END","ENd", "enD", "eND", "eNd", "EnD"]:     ### For the first time ... I loved it !!! ###
        break
    else:
        try:
            item = int(item)
            my_list.append(item)
        except:
            continue

my_list.sort()
print(my_list)   ### Check !! ###

### End of input routine ###


### Action !!! ###

my_new_list = del_repeated(my_list)
my_new_list.sort()
print("Lista nova modificada: ", my_new_list)

print ("\n\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")