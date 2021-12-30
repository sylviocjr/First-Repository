### 27 Dec., 2021 ###
### Exercise 01 week 7 Coursera Python ###
### Printing a hollow rectangle using two loops ###

### Key words: print() function; loops using while ###
### This program prints a hollow rectangle given its width and height ###

### Palavras-chave: função print(); iterações usando while ###
### Este script imprime um retângulo a partir de sua largura e altura, usando a função print() e caractere '#' ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###
    

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))


cont = 1
while cont <= altura:
    cont1 = 1
    while cont1 <= largura:
        if cont == 1 or cont == altura:
            print("#", end = "")
        else:
            print("#"+(largura-2)*" "+ "#",end = "")   ### Concatenação ###
            break
        cont1+=1
    print()
    cont+=1

print ("\n\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")
