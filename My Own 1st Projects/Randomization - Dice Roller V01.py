# Nov.18, 2021
# Randomization - chapter. 4 Python Book
# This script simulates a dice roller, by means of Python functions using randomization. Also, the script
# enables the user to choose how many times he/she wants to roll a cubic dice.
# Two different ways to ramdomize were used for instructional purposes: random.randint e random.choice
# For this moment, I'm using only keybord inputs because I am a novice student of Python.

# 18 nov. 2021
# Randomização - cap. 4
# Objetivo: simular um jogo de dado. Possibilitar ao jogador que escolha
# quantas vezes deseja jogar o dado.
# Usadas duas formas de randomização: random.randint e random.choice

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

import random # Fundamental !!!

times=input("How many times do you wish to roll the cubic dice? ")
times=int(times)
for i in range(times):
    y = random.randint(1,6)
    print(y, end=' ')

print()
print("Let's try once more ...")
times=input("How many times do you wish to roll the cubic dice? ")
times=int(times)
faces = [1,2,3,4,5,6]
for i in range(times):
    z = random.choice(faces)
    print(z, end=' ')

print("\n\n### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###")
