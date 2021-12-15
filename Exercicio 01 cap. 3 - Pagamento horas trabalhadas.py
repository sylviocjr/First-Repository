# 10 nov. 2021
#Exercício 01 Capítulo 3
#Uso de input, int() e float(). Observar bem o uso das funções int() e float()
#Digitar valor inteiro para "horas". Digitar valor real para "valor_hora"

horas=input("Horas trabalhadas:")
valor_hora=input("Valor hora:")

horas=int(horas)
valor_hora=float(valor_hora)
adicional=0
pagamento=0

# A seguir, rotina para cálculo em caso de o número de horas ser menor
# ou igual a 40 horas, o que levaria a erro de cálculo se aplicada uma fórmula
# genérica como a utilizada a partir do "else" a seguir, onde (horas - 40)
# resultaria em valor negativo, gerando desconto indevido :

if horas <= 40:
    pagamento = horas*valor_hora

# A seguir, cálculo específico para a situação de mais de 40 horas

else:
	pagamento=40*valor_hora
	adicional=(horas - 40)*valor_hora*1.5
	pagamento = pagamento + adicional

print("Honorarios a pagar: ",pagamento)
