### Dec. 19, 2021 ###
### Exercise for Coursera week 5 ###
### Key words: division; divisor; divisibility; remainder; functions; Python functions ###
### This program shows if a given number is either divisible by 3 or 5, or if it's divisible for both 3 and 5 ###

### Palavras-chave: divisão; divisor; divisibilidade; resto de uma divisão; funções; funções em Python ###
### Este programa exibe se um dado número é divisível por 3 ou por 5, ou se é ao mesmo tempo divisível por 3 e 5 ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

def fizzbuzz(x):
    if (x % 3 == 0) and (x % 5 != 0):
        return "Fizz"
    elif (x % 3 != 0) and (x % 5 == 0):
        return "Buzz"
    elif (x % 3 == 0) and (x % 5 == 0):
        return "FizzBuzz"
    elif (x % 3 != 0) and (x % 5 != 0):
        return x

def main():
    numero = int(input('Digite o número: '))
    print(fizzbuzz(numero))

    print()
    print('Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil')

main()
