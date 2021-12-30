### 27 Dec., 2021 ###
### Exercise 01 week 7 Coursera Python ###
### Printing a full rectangle using two loops ###

### Key words: print() function ###
### This program prints a full rectangle given its width and height ###

### Palavras-chave: função print() ###
### Este script imprime um retângulo a partir de sua largura e altura, usando a função print() e caractere '#' ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###
    

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))


cont = 1
while cont <= altura:
    cont1 = 1
    while cont1 <= largura:
        print("#", end = "")
        cont1+=1
    print()
    cont+=1

print ("\n\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")
