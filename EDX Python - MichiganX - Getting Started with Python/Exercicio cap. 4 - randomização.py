# 15 nov. 2021

# Randomização - cap. 4

import random # Fundamental !!!

print ("Geração de 10 randômicos conf. função 'random'")
for i in range(10):
    x = random.random()
    print(x)

# O nome "i" para a variável contadora é aleatório. Pode receber outros
# nomes quaisquer não conflitantes.

print() # Pula linha

print ("Geração de 10 randômicos conf. função 'randint' (inteiros)")
for i in range(10):
    y = random.randint(1,10)
    print(y)

print() # Pula linha

FIB = [0,1,1,2,3,5,8,13,21,34] # Seq. Fibonacci - poderia ser qualquer outra
for i in range(10):
    z = random.choice(FIB)
    print(z)
