# 07 nov. 2021
#Exercício análogo ao exercício 03 da página 12 Capítulo 2
#Uso de input, int() e float(). Observar bem o uso das funções int() e float()
#Digitar valor inteiro para "horas". Digitar valor real para "valor_hora"

horas=input("Horas trabalhadas:")
valor_hora=input("Valor hora:")
horas=int(horas)
valor_hora=float(valor_hora)
print("Honorarios a pagar: ",horas*valor_hora)
