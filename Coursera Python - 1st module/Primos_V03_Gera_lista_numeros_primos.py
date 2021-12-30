### 02 dez. 2021 ###
### Números primos - V. 03 ###
### Gera uma lista de números primos até o limite definido pelo usuário ###



limite = input("Digite o limite superior da lista: ")
limite = int(limite)

print("Eis os números primos até", limite, ":")
print(2) ### Força a impressão do 2, que não se enquadra na rotina abaixo ###

dividendo = 3   ### Primeiro dividendo considerado, uma vez que 2 não cumpre a rotina abaixo ###

for i in range (limite-2):
      
        
        divisor = 2

        for j in range(dividendo - 2):
                resto = dividendo % divisor
                if resto == 0:
                        #print(dividendo, "Não Primo")
                        break
                else:
                        #print(dividendo, "dividiu por ", divisor)
                        divisor = divisor+1
        if resto !=0:
                print(dividendo)

        dividendo = dividendo + 1

### Se possível, numa próxima versão, imprimir os resultados somente ao final, depois de armazenados os primos em vetores. ###
