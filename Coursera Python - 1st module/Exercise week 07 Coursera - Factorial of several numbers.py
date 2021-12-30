### Dec. 24, 2021 ###
### Factorial of several int. numbers ###
### Fatorial de diversos números ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

def funcao_fatorial(n):
    if n < 0:
        return 0
    fatorial = proximo = 1

    while proximo <= n:
        fatorial = fatorial * proximo
        proximo +=1

    return fatorial

print('\n\n**** Factorial of an integer number equal or greater than zero ****', end = '\n\n')
while True:
    numero = input("Input an integer number (or 'end' to quit): ")
    if numero == 'end' or numero == 'End' or numero == 'END':
        break
    else:
        numero = int(numero)
        fat_numero = funcao_fatorial(numero)
        print('Factorial of',numero,':', fat_numero, end = '\n\n')

print('\nEnd of this program. See You !')
print('\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil')
