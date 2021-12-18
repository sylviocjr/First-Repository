### Dec. 18, 2021 ###
### Exercise for Coursera week 5 ###
### Key words: Prime numbers; functions; Python functions ###
### This program calculates and returns the largest prime number,  less than or equal to a number given by the user ###

### Palavras-chave: Números primos; funções; funções em Python ###
### Este programa calcula e retorna o maior número primo, menor ou igual a um dado número informado pelo usuário ###

### Sylvio Carneiro Junior - sylviocr.dev@gmail.com - Santa Catarina, Brazil ###

def primo(a):   ### Verifica se o parâmetro passado é primo ###
    divisor = 2
    cont=1
    resto = 1  ### Força a situação no caso de ser informado o número 2, executando a partir de " if resto != 0: "
    while cont <= (a - 2):   ### Não executa para 2 ! ###
        resto = a % divisor
        if resto == 0:
            return False
        divisor += 1
        cont += 1
    if resto != 0:
        return True


def maior_primo(b):   ### Conterá o looping ###
    cont1 = 2
    while cont1 <= b:
        is_prime = primo(cont1)
        if is_prime == True:
            maior_nr_primo = cont1
        cont1 += 1
    return maior_nr_primo

### Entradas validadas ###
def main():
    dividendo = 1    ### Força a entrada no loop a seguir: ###
    while dividendo < 2:
        try:
            dividendo = int(input("Informe o número inteiro, primo ou não, maior ou igual a 2: "))
            if dividendo < 2:
                print('Entrada inválida !!')
            if dividendo >= 2:
                print('Maior primo anterior ou igual a', dividendo, 'é', maior_primo(dividendo))

        except:
            print('Entrada inválida !!')

    print()
    print('Sylvio Carneiro Junior - sylviocr.dev@gmail.com - Santa Catarina, Brazil')

main()
