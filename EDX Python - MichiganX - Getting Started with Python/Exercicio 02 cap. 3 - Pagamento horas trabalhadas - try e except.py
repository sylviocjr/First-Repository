# 11 nov. 2021
#Uso de try e except
#Digitar valor inteiro para "horas". Digitar valor real para "valor_hora"

horas = 0
valor_hora = 0

horas=input("Horas trabalhadas:")
valor_hora=input("Valor hora:")

try:
	print("Honorarios a pagar: ",int(horas)*float(valor_hora))
except:
	print("Erro ! Digite um valor numérico:")
