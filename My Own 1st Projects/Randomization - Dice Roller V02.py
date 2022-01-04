# Nov.18, 2021
# Randomization - chapter. 4 Python Book
# This script simulates a dice roller, by means of Python functions using randomization. Also, the script
# enables the user to choose how many times he/she wants to roll a cubic dice.
# Also, it calculates the statistical frequency observed for every single face of the dice and compares
# with the probability of ocurrence for every face, considering here a cubic dice.
# Experiment with different large numbers for every try. Observe the results and the time required
# to generate these results as your number of times increases.
# For this moment, I'm using only keybord inputs because I am a novice student of Python.

# Calcular a frequência de cada número sorteado e comparar com
# a probabilidade estatística de ocorrer cada número.
# Experimentar com diferentes números grandes de vezes de jogadas !!!
# Observar o tempo que leva para gerar o resultado à medida em que número
# de vezes aumenta significativamente

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

import random # Fundamental !!!

count1=count2=count3=count4=count5=count6=0
while True:
    try:
        times=input("How many times do you wish to roll the cubic dice? ")
        times=int(times)
    except:
        continue
    if times >= 1:
        break
    else:
        continue

for i in range(times):
    face = random.randint(1,6)
    if face == 1:
        count1=count1+1
    elif face == 2:
        count2=count2+1
    elif face == 3:
        count3=count3+1
    elif face == 4:
        count4=count4+1
    elif face == 5:
        count5=count5+1
    elif face == 6:
        count6=count6+1

print("\n'Δ' represents the difference between the frequency of ocurrence and the probability of ocurrence for every face.\n")
print("Face 1 ocurred", count1, "time(s)\t", (count1/times)*100, "%\t", "\tΔ =", ((count1/times)-(1/6)))
print("Face 2 ocurred", count2, "time(s)\t", (count2/times)*100, "%\t", "\tΔ =", ((count2/times)-(1/6)))
print("Face 3 ocurred", count3, "time(s)\t", (count3/times)*100, "%\t", "\tΔ =", ((count3/times)-(1/6)))
print("Face 4 ocurred", count4, "time(s)\t", (count4/times)*100, "%\t", "\tΔ =", ((count4/times)-(1/6)))
print("Face 5 ocurred", count5, "time(s)\t", (count5/times)*100, "%\t", "\tΔ =", ((count5/times)-(1/6)))
print("Face 6 ocurred", count6, "time(s)\t", (count6/times)*100, "%\t", "\tΔ =", ((count6/times)-(1/6)))
print("\n\n### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###")
