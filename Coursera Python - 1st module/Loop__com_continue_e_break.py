

# Caso o primeiro caractere da palavra digitada for "#", esta palavra não será impressa na tela.
# Caso o segundo caractere da palavra digitada for "#", esta palavra não será impressa na tela.

while True:
    linha = input('Escreva qualquer coisa (ou "sair"): ')
    if linha[0] == '#':    #Observar a indicação para o PRIMEIRO caractere entre colchetes !!
        continue
    if linha[1] == '#':    #Observar a indicação para o SEGUNDO caractere entre colchetes !!
        continue
    if linha == 'sair':
        break
    print(linha)
print('Tchau !!')
