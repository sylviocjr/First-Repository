### 18 dez. 2021 ###
### Função Número primo ###
### A partir de um número inteiro informado, a função retorna se o número é ou não primo ###
### Implementação e chamada da função main() pela primeira vezem exercícios ###


def primo(a):
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

def main():
    dividendo = 1    ### Força a entrada no loop a seguir: ###
    while dividendo < 2:
        try:
            dividendo = int(input("Informe o número inteiro, primo ou não, maior ou igual a 2: "))
            if dividendo < 2:
                print('Entrada inválida !!')
            if dividendo >= 2 and primo(dividendo) == True:
                print(dividendo, 'é primo !')
            elif dividendo >= 2 and primo(dividendo) == False:
                print(dividendo,'NÃO é primo !!')
        except:
            print('Entrada inválida !!')
        
main()    ### Somente neste ponto a função main() é chamada !! ###
