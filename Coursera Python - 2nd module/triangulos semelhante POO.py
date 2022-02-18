'''
Feb 05, 2022
OOP additional homework 02 week 03 Coursera Python 2nd phase

For my own instructional purposes only.

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        if triangulo.a / self.a == triangulo.b / self.b and triangulo.b / self.b == triangulo.c / self.c:
            return True
        else:
            return False

# Aprovado no teste. Aprimorar, seguindo a sugestão da tarefa, ordenando os parâmetros, caso os
# triângulos sejam semelhantes, mas os parâmetros não estejam em ordem de forma a identificar
# a semelhança.