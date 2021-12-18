### 06 dez. 2021 ###
### Ex. 04 cap. 06 ###


palavra = 'banana'

letra_a = palavra.count('a')
letra_n = palavra.count('n')

print(letra_a, "a")
print(letra_n, "n")

outra_palavra = input("digite uma palavra: ")
letra_qqer = input("digite uma letra para pesquisa: ")
vezes = outra_palavra.count(letra_qqer)

print("A letra", letra_qqer, "aparece", vezes, "vez(es) em", outra_palavra)
