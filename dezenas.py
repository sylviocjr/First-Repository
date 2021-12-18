
### 01 dez. 2021
### Exercícios adicionais 03 - Dígito das dezenas

numero = input("Digite um número inteiro:")
numero = int(numero)
numero = numero/100
parte_inteira = int(numero)
#print("Parte inteira:", parte_inteira)
parte_decimal = numero - parte_inteira
#print("Parte decimal:", parte_decimal)
dezenas_e_unidades = parte_decimal*100
#print("Dezenas e unidades:", int(dezenas_e_unidades))
dezenas = dezenas_e_unidades//10
print("O dígito das dezenas é", int(dezenas))
