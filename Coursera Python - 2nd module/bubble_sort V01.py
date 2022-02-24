'''
Feb 23, 2022
Bubble Sort program - Version 01

For my own instructional purposes only.

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

list = [5,1,4,2]  # Type here your list of integer numbers ...
end = len(list)
for i in range(end - 1, 0, -1):
    for j in range(i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            

print(list)
