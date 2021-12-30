### 05 dez. 2021 ###
### Exercício 01 cap. 5 ###
### Fazer leituras repetidas de vários números até o usuário digitar "fim" ###
### Fazer a contagem das entradas, soma total e média ###
### Acusar erro se o usuário entrar outro dado além de número ou "fim" ###

# Variáveis: numero; contador; soma;

soma = contador = 0

while True:
    numero = input("Digite um número qualquer ou 'fim' para sair: ")
    try:
        if numero == "fim" or numero == "Fim" or numero == "FIM" or numero == "FIm" or numero == "FiM" or numero == "fIm" or numero == "FIm" or numero == "fiM":
            break
        else:
            numero = float(numero)
            contador = contador + 1
            soma = soma + numero
    except:
        print("Erro ! Comece novamente !")

### Fim while


print ("Fim ! Vamos aos resultados: ")
print("Foram digitados", contador, "números.")
print ("Soma dos números :", soma)
if contador != 0:
    print ("Média dos números :", (soma/contador))
elif contador == 0:
    print ("Média não disponível !")

