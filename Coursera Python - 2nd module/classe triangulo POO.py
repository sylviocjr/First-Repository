'''
Feb 05, 2022
OOP homework 01 week 03 Coursera Python 2nd phase

For my own instructional purposes only.

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

# Programa:

lado_a = int(input("Lado A: "))
lado_b = int(input("Lado B: "))
lado_c = int(input("Lado C: "))

t = Triangulo(lado_a, lado_b, lado_c)
print(t.perimetro())
