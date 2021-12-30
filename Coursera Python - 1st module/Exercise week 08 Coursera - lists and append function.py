
### 28 Dec., 2021 ###
### Lists and append function ###
### Exercise from the video class - Coursera week 08 ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

lista = []   ### Inicializa uma lista vazia ###

item = 1
while item != 0:
    item = int(input("Digite um número (0 p/ sair): "))
    if item != 0:
        lista.append(item)

    
print ("\nElementos da lista, em ordem inversa: ")

i = 1
while i <= (len(lista)):
    print (lista[-i], end = " ")   
    i+=1
### Esta forma, de indexar com índice negativo nos colchetes ([-i]), tornou a lógica e a leitura mais intuitivas ###

print("\n\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")
