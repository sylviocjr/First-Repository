# 18 nov. 2021

# Randomização - cap. 4
# 18 nov. 2021

# Randomização - cap. 4
# Objetivo: simular um jogo de dado. Possibilitar ao jogador que escolha
# quantas vezes deseja jogar o dado.
# Usadas duas formas de randomização: random.randint e random.choice

import random # Fundamental !!!

vezes=input("Quantas vezes deseja jogar o dado ?")
vezes=int(vezes)
for i in range(vezes):
    y = random.randint(1,6)
    print(y)

print()
print("Novamente ...")
vezes=input("Quantas vezes deseja jogar o dado ?")
vezes=int(vezes)
faces = [1,2,3,4,5,6]
for i in range(vezes):
    z = random.choice(faces)
    print(z)
