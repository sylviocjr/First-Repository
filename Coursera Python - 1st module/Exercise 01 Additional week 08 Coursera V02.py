### Jan. 5th, 2022 ###
### Exercise 01 Additional week 08 Coursera Python ###
### Returning the highest value from a list of integers ###

### Key words: lists; functions ###
### This script in Python creates a list from integers given by the user and, by means of a function, returns the highest value from the list ###

### Palavras-chave: listas; funções ###
### Este script em Python cria uma lista a partir de números inteiros fornecidos pelo usuário e retorna o maior valor da lista ###

### Elaborar a versão para entrega: textos conforme template do exercício e eliminar itens não solicitados ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###


def highest_value(list):
    highest = list[0]
    i = 1
    while i <= (len(list)-1):
        if highest < list[i]:
            highest = list[i]
        i+=1
    return (highest)


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

#my_list.sort()
print("Here's your list: ", my_list)   ### Check !! ###

### End of input routine ###


### Action !!! ###

print("Highest value in the list: ", highest_value(my_list))

print ("\n\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")