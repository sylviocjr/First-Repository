# 15 nov. 2021

# Observar que a função "int" não arredonda o valor de seu retorno !!
# Ver também que ela retorna a parte inteira do argumento e descarta a
# parte decimal. Ver nos cálculos abaixo:

x = int(3.999999999)
print(x)
print(x*10)
print(x*100)
print(x*1000)

y = int(2.3)
print(y)
print(y*10)
print(y*100)
print(y**2)
print(y**3)

numero_qualquer = 12345 # Valor numérico
print (numero_qualquer * 1000) # Cálculo com o valor anterior, provando que
# é numérico
STRING = str(numero_qualquer) # Transforma a sequência numérica em string.
print(STRING + " string literal - não permite cálculos !")
