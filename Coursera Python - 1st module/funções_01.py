# 21 nov. 2021
# Primeiro script usando Idle
# Criação de funções


def calcula_salario(a,b):
    c = a*b
    return c

variavel_iteracao = 1

while variavel_iteracao == 1:
    try:
    
        horas = input("Informe horas trabalhadas: ")
        horas = int(horas)
    
        valor_hora = input("Informe valor da hora trabalhada: ")
        valor_hora = float(valor_hora)
    
        honorarios = calcula_salario(horas, valor_hora) # Neste ponto é chamada a função !! Observar a variável atribuída ao resultado da chamada da função.
    
        print("Honorários a pagar: R$ ", honorarios)

        variavel_iteracao = 0   # Assinala para o fim do loop
    
    except:
        print("ERRO !!! Informe um valor válido !!")


