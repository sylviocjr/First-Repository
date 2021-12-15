# 11 nov. 2021
#Uso de try e except - 2a versão - observar a lógica
#Digitar valor inteiro para "horas". Digitar valor real para "valor_hora"

horas = 0
valor_hora = 0

horas=input("Horas trabalhadas:")
try:
	horas=int(horas)
	valor_hora=input("Valor hora:")
	valor_hora=float(valor_hora)
	print("Honorarios a pagar: ",int(horas)*float(valor_hora))
except:
	print("Erro ! Digite um valor numérico:")
