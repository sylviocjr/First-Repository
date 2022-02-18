'''
Jan. 19 2022.
Randomization - chapter. 4 Python Book
Adapted example of simulation using pseudorandom numbers shown on pages 24 to 28 of the book "Pesquisa Operacional 
- UnisulVirtual" (Operatinal Research) used by the students of the Bachelor's degree in Mathematics at Universidade
do Sul de Santa Catarina (Brazil).
This script uses pseudorandom numbers to simulate the expected profit from selling a given quantity of apple pies
considering the quantity of pies that are supposed to be made versus the demand of this product.
The seller expends $ 7.50 and earns $ 12.00 for each apple pie. The left over pies are sold at $ 6 in order to
reduce the losses.
The seller wishes to maximize his profit considering different scenarios of making 40, 50, 60, 70, 80 or 90 apple
pies and the demand isn't known, being estimated by means of randomization from 1 to 6, just like rolling a dice.
The random number 1 represents a demand of 40 pies. The random number 2 represents 50 pies and so on, what can be
seen along the code.
At the end, the program shows the average profit considering a given quantity of apple pies to be made. The higher
the quantity of simulations, the better and more accurate are the results.
For this moment, I'm using only keybord inputs because I am a novice student of Python.
This program is only intended to improve my skills in Python (novice level) as well as practice those homeworks
of my Bachelor's degree in Mathematics, which I consider very interesting to be implemented using Python. So, every
routine of this code can be modified at any moment, introducing new skills that I learn during my classes.
'''

# 19 jan. 2022.
# Randomização - cap. 4
# Objetivo: simular um ...

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

import random # Fundamental !!!

'''def returns_demand(x):
    if x == 1:
        demand = 40
    elif x == 2:
        demand = 50
    elif x == 3:
        demand = 60
    elif x == 4:
        demand = 70
    elif x == 5:
        demand = 80
    elif x == 6:
        demand = 90
    return demand
    '''


# Rotina de validação da entrada numérica - Quantidade de simulações:
times = ''  # Initialization of 'times' non numeric in order to start the next 'while loop'.
while not times.isnumeric():
    times = input("How many times do you wish to simulate profit? (The more, the better!): ")
times = int(times)

qty_pies_table = ['40','50','60','70','80','90']

table =[[0, 0],  # This line [0,0] will not be used ... it was created to handle the indexes from 1 to 6 more easily.
        [1,40],
        [2,50],
        [3,60],
        [4,70],
        [5,80],
        [6,90]]  # Matriz com correspondências para este problema em particular


# Rotina de validação da entrada numérica - Quantidade de encomendas de tortas:
qty_pies = '0'  # Initialization of 'qty_pies' non numeric in order to start the next 'while loop'.
while not qty_pies in qty_pies_table:
    qty_pies = input("Enter quantity of apple pies you wish to sell (Choose one of 40, 50, 60, 70, 80, 90): ")
qty_pies = int(qty_pies)

profit = 0
i = 1
while i <= times:
    j = random.randint(1,6)
    # print(j)  # Check
    demand = table[j][1]  # Bingo !!!
    # print("Demanda: ", demand)  # Check
    

    if demand >= qty_pies:
        profit = profit + (4.5*qty_pies)  # $ 4.50 = $ 12.00 - $ 7.50
    else:
        profit = profit + (6*demand - 1.5*qty_pies)
    i += 1

print("\nAverage Profit: ${:.2f}".format(profit/times))

print("\n\n### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###")
