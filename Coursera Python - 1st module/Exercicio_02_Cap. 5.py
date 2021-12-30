### 05 dez. 2021 ###
### Exercício 02 cap. 5 ###
### Fazer leituras repetidas de vários números até o usuário digitar "fim" ###
### Fazer a contagem das entradas, soma total e listar o maior e menor número ###
### Acusar erro se o usuário entrar outro dado além de número ou "fim" ###

# Variáveis: numero; contador; soma; maior; menor

soma = contador = 0

### Rotina de inicialização, sem considerar poossibilidade de iniciar com "fim" ou entrada imprevista. Apenas para verificar a lógica. ###

numero = input("Digite um número qualquer para começar: ")
menor = maior = numero = int(numero)
contador = contador + 1
soma = soma + numero

##############################################################################################

while True:
    numero = input("Digite um número qualquer ou 'fim' para sair: ")
    try:
        if numero == "fim" or numero == "Fim" or numero == "FIM" or numero == "FIm" or numero == "FiM" or numero == "fIm" or numero == "FIm" or numero == "fiM":
            break
        else:
            numero = int(numero)
            contador = contador + 1
            soma = soma + numero
            if numero > maior:   ### Rotina para identificar o maior dentre os números ###
                maior = numero
            if numero < menor:   ### Rotina para identificar o menor dentre os números ###
                menor = numero
    except:
        print("Erro ! Comece novamente !")

### Fim while


print ("Fim ! Vamos aos resultados: ")
print("Foram digitados", contador, "números.")
print ("Soma dos números :", int(soma))
if contador != 0:
    print ("Maior dos números :", int(maior))
    print ("Menor dos números :", int(menor))

elif contador == 0:
    print ("Maior e menor número não disponíveis !")

