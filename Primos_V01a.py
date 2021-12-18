### 02 dez. 2021 ###
### Números primos - V. 01 ###
### A partir de um número inteiro informado, o script calcula e informa se o número é ou não primo ###


dividendo = int(input("Informe o número inteiro primo ou não: "))
divisor = 2
cont=1
resto = 1  ### Força a situação no caso de ser informado o número 2, executando a partir de " if resto != 0: "

while cont <= (dividendo - 2):   ### Não executa para 2 ! ###
        resto = dividendo % divisor
        #print(resto)
        if resto == 0:
                print(dividendo, "não é primo !!!")
                break
        divisor = divisor + 1
        cont += 1

if resto !=0:
        print(dividendo, "é primo !!!")


### Próximo desafio: listar todos os divisores, caso o número não seja primo. ###

