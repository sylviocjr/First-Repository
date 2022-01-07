### Jan. 04, 2022 ###
### Exercise 01 week 08 Coursera Python ###
### Sorting a list and deleting repeated elements from a list ###

### Key words: ... ###
### This program creates a list from integers given by the user, delete repeated elements from this list and sorts the elements ###

### Palavras-chave: ... ###
### Este script cria uma lista a partir de números inteiros fornecidos pelo usuário, elimina os valores repetidos e ordena a lista ###

### Elaborar a versão para entrega: textos conforme template do exercício e eliminar itens não solicitados ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###



my_list = []


### Input Routine ###

while True:
    item = input("Enter an integer number to the list ('end' to exit): ")
    if item == "end" or item == "End" or item == "END":
        break
    else:
        try:
            item = int(item)
            my_list.append(item)
        except:
            continue

#my_list.sort()
print(my_list)   ### Check !! ###

### End of input routine ###

### Action !!! ###

other_list = my_list[:]
#other_list.sort()
print("Outra lista clonada: ", other_list)

final_list=[]

i = 0
while i <= len(my_list):
    if my_list[i] in other_list:
        final_list.append(my_list[i])
        i+=1


print("Lista final gerada: ", final_list)


print ("\n\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")