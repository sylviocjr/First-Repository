# 23 nov. 2021
# Programa cálculo de IMC usando funções

def calcula_IMC(w,h):
    indice = w/h**2
    return(indice)


peso = input("Digite o peso em Kg: ")
peso = int(peso)

altura = input("Digite a altura em 'm': ")
altura = float(altura)

IMC = calcula_IMC(peso,altura)
print("Peso :", peso, "Kg")
print("altura :", altura*100, "cm")
print("IMC: ",IMC)
