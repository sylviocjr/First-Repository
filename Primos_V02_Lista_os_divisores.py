### 02 dez. 2021 ###
### Números primos - V. 02 ###
### A partir de um número inteiro informado, o script calcula e informa se o número é ou não primo, além de informar seus divisores ###


dividendo = input("Informe o número inteiro primo ou não: ")
dividendo = int(dividendo)
divisor = 2
numeroDivisores = 0
i = 1

for i in range(dividendo - 2): ### Não executa para 2 ! ###
        resto = dividendo % divisor
        if resto == 0:
                numeroDivisores = numeroDivisores + 1
                #print("TESTE")
                print("Divisor: ", divisor)
        divisor = divisor + 1

if numeroDivisores == 0:
        print(dividendo, "é primo !!!")
else:
        print(dividendo, "NÃO é primo e tem", numeroDivisores, "divisores !")


### Próximo desafio: listar todos os divisores em um vetor e listar somente ao final, caso o número não seja primo. ###
    
    
