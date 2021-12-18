### 07 dez. 2021 ###
### Exercício 05 cap. 6 ###


str = 'X-DSPAM-Confidence:0.8475'

print('A string a ser tratada é: ', str)  # check #

posicao = str.find(':')
print("A posição do caractere ':' é: ",posicao) # check #
print("Esta posição calculada é do tipo", type(posicao)) # check #

numero = str[posicao+1:]
print(numero, 'ainda na forma string. Veja: ', numero+' é string !')
print("A string numérica gerada é do tipo", type(numero)) # check #

numero = float(numero)
print('Agora já convertemos a string numérica para float. Veja: ',type(numero))
print('alguns cálculos para verificação:')
print('Número x 10: ', numero*10) # check #
print('Número x 100: ',numero*100) # check #
print('Número / 10: ',numero/10) # check #
