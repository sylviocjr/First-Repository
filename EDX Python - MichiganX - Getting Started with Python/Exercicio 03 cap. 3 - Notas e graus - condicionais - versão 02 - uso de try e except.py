# 12 nov. 2021
# Exercício 03 Capítulo 03
score=0
score=input("Digite uma nota:")
try:
	score=float(score)
	if score < 0.0 or score > 1.0:
		print ("Erro ! Nota inválida !!")
	elif score >=0.9 and score <= 1.0:
		grau="A"
	elif score >=0.8 and score < 0.9:
		grau="B"
	elif score >=0.7 and score < 0.8:
		grau="C"
	elif score >=0.6 and score < 0.7:
		grau="D"
	else:
		grau="F"
	print("Seu grau :",grau) # Aqui está o erro. A variável grau não recebe
	# valores se atendidas as condições da linha 7.

except:
	print("Erro !!!")

# Bug desta versão: para as notas numéricas inválidas condicionadas na linha 7,
# o programa deixa de executar as linhas de 9 a 18 e se depara com uma
# inconsistência na linha 19, uma vez que a variável "grau" não recebeu
# valores, conforme deveria ocorrer normalmente de 9 a 18. Assim, diante desta
# inconsistência, o programa encontra um erro, que o faz executar também o
# conteúdo do bloco "except", passando a exibir duas mensagens de erro.
# O conteúdo do bloco "except" passa a ser executado a partir de qualquer
# ponto onde o programa encontra erro ou inconsistência, mesmo que ao final.
