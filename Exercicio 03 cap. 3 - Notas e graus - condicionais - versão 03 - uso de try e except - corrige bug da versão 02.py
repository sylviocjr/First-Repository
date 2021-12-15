# 12 nov. 2021
# Exercício 03 Capítulo 03
score=0
score=input("Digite uma nota:")
try:
	score=float(score)
	if score >=0.9 and score <= 1.0:
		grau="A"
		print("Seu grau :",grau)
	elif score >=0.8 and score < 0.9:
		grau="B"
		print("Seu grau :",grau)
	elif score >=0.7 and score < 0.8:
		grau="C"
		print("Seu grau :",grau)
	elif score >=0.6 and score < 0.7:
		grau="D"
		print("Seu grau :",grau)
	elif score >= 0 and score < 0.6:
		grau="F"
		print("Seu grau :",grau)
	elif score < 0.0 or score > 1.0:
		print("Erro ! Nota inválida !!")

except:
	print("Erro !!!")
