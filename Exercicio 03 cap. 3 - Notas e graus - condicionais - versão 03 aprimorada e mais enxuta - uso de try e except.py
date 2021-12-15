# 12 nov. 2021
# Exercício 03 Capítulo 03
score=0
score=input("Digite uma nota:")
try:
	score=float(score)
	if score >= 0.0 and score <= 1.0: #Esta verificação já remete à mensagem de erro caso a entrada numérica esteja fora dos limites !
		if score >=0.9 and score <= 1.0:
			grau="A"
		elif score >=0.8 and score < 0.9:
			grau="B"
		elif score >=0.7 and score < 0.8:
			grau="C"
		elif score >=0.6 and score < 0.7:
			grau="D"
		elif score >=  0 and score < 0.6:
			grau="F"
	print("Seu grau :",grau)
except:
	print("Erro !!!")

# Versão aprimorada e mais enxuta
