# 18 nov. 2021

# Randomização - cap. 4
# Jogando dados V02
# Objetivo: simular um jogo de dado. Possibilitar ao jogador que escolha
# quantas vezes deseja "jogar o dado".
# Calcular a frequência de cada número sorteado e comparar com
# a probabilidade estatística de ocorrer cada número.
# Experimentar com diferentes números grandes de vezes de jogadas !!!
# Observar o tempo que leva para gerar o resultado à medida em que número
# de vezes aumenta significativamente

import random # Fundamental !!!

cont1=cont2=cont3=cont4=cont5=cont6=0

vezes=input("Quantas vezes deseja jogar o dado ?")
vezes=int(vezes)
for i in range(vezes):
    face = random.randint(1,6)
    if face == 1:
        cont1=cont1+1
    elif face == 2:
        cont2=cont2+1
    elif face == 3:
        cont3=cont3+1
    elif face == 4:
        cont4=cont4+1
    elif face == 5:
        cont5=cont5+1
    elif face == 6:
        cont6=cont6+1

#    print(face)      # Deixar como opcional a impressão dos resultados,
# especialmente se houver um número grande de jogadas.

print("Face 1 ocorreu", cont1, "veze(s),", (cont1/vezes)*100, "%,", "Δ =", ((cont1/vezes)-(1/6)))
print("Face 2 ocorreu", cont2, "veze(s),", (cont2/vezes)*100, "%,", "Δ =", ((cont2/vezes)-(1/6)))
print("Face 3 ocorreu", cont3, "veze(s),", (cont3/vezes)*100, "%,", "Δ =", ((cont3/vezes)-(1/6)))
print("Face 4 ocorreu", cont4, "veze(s),", (cont4/vezes)*100, "%,", "Δ =", ((cont4/vezes)-(1/6)))
print("Face 5 ocorreu", cont5, "veze(s),", (cont5/vezes)*100, "%,", "Δ =", ((cont5/vezes)-(1/6)))
print("Face 6 ocorreu", cont6, "veze(s),", (cont6/vezes)*100, "%,", "Δ =", ((cont6/vezes)-(1/6)))
