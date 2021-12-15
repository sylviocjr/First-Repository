# 12 nov. 2021
# Exercício 03 Capítulo 03

score=input("Digite uma nota:")
score=float(score)
#
if score >=0.9 and score <= 1:
  grau="A"
elif score >=0.8 and score < 0.9:
  grau="B"
elif score >=0.7 and score < 0.8:
  grau="C"
elif score >=0.6 and score < 0.7:
  grau="D"
else:
  grau="F"
print("Seu grau :",grau)
