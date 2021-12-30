### 09 dez. 2021 ###

soma_digitos = 0

while True:
    soma_digitos = 0
    numero = input("Número (fim p/ sair): ")
    try:
        if numero == 'fim':
            break
        else:
            numero=int(numero)
            if numero < 0:   ### Corrige para o caso de o número digitado ser negativo ###
                numero *=(-1)
                
        while True:   
            unidade = numero % 10
            soma_digitos += unidade
            #print("Unidade: ", unidade)
            numero -= unidade
            #print ("Sobra :", numero)
            numero /= 10
            #print("Novo numero: ", int(numero))
            if numero % 10 == 0 and numero < 10:   ### Segunda comparação evita Bug em caso de numeros que terminam com sequência de zeros ###
                break
        print("Soma dos dígitos: ", int(soma_digitos))
    except:
        continue
