### 02 dez. 2021 ###
### Números primos - V. 01 ###
### A partir de um número inteiro informado, o script calcula e informa se o número é ou não primo ###


dividendo = input("Digite um número inteiro: ")
dividendo = int(dividendo)
divisor = 2
i=1
resto = 1  ### Força a situação no caso de ser informado o número 2, executando a partir de " if resto != 0: "

for i in range(dividendo - 2):   ### Não executa para 2 ! ###
        resto = dividendo % divisor
        #print(resto)
        if resto == 0:
                print("não primo")
                break
        divisor = divisor + 1

if resto !=0:
        print("primo")


### Próximo desafio: listar todos os divisores, caso o número não seja primo. ###

