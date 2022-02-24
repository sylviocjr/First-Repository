'''
Feb 23, 2022
Bubble Sort program - Version 02 - Function Bubble Sort

For my own instructional purposes only.

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

def bubble_sort(list):
    end = len(list)
    for i in range(end - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(list)
    return(list)
