
### 06 dez. 2021 ###
### Ex. 03 cap. 6 ###

def count(a,b):
    palavra = a
    cont = 0
    for letra in palavra:
        if letra == b:
            cont = cont + 1
    return cont


palavra_qqer = input("Digite uma palavra qualquer: ")
caractere = input("Informe o caractere para pesquisa: ")

vezes = count(palavra_qqer,caractere)

if vezes == 1:
    print("O caractere", caractere, "aparece", vezes, "vez na palavra.")   ### Ajuste gramatical para apenas uma ocorrência ###

elif vezes == 0:
    print("O caractere", caractere, "não foi encontrado na palavra.")   ### Ajuste gramatical para nenhuma ocorrência ###

else:
    print("O caractere", caractere, "aparece", vezes, "vezes na palavra.")   
