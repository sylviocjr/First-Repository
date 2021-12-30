### 07 dez. 2021 ###
### Exercícios gerais - Funções ###

### Obs: a função radiciação não funciona para radicandos negativos !! Pesquisar motivo. Retorna valor complexo. ###

# -----------------------
def funcao_quadrado(x):
    return x**2
# -----------------------

# -----------------------
def funcao_potencia(y,z):
    return y**z
# -----------------------

# -------------------------
def funcao_radiciacao(p,q):
    return (p**(1/q))
# -------------------------

#------------------ Quadrado de um número ----------------------

base = float(input('Digite um n° para elevar ao quadrado: '))
quadrado = funcao_quadrado(base) # chamada à função ...
print('Quadrado de', base, 'é: ',quadrado)
# --------------------------------------------------------------

#---------------- Exponenciação --------------------------------
numeros = input("Digite base e expoente, separados por ';': ")
indice = numeros.find(';')
#print(indice) # check #

base_exp = float(numeros[:indice])

#print(base_exp*10) # check #

expoente = float(numeros[indice+1:])

#print(expoente*10) # check #

potencia = funcao_potencia(base_exp,expoente) # chamada à função ...
print('A base',base_exp, 'elevada a', expoente, 'é: ', potencia)
# --------------------------------------------------------------

#------------------ Raiz enézima -------------------------------
numeros = input("Digite o radicando e o índice da raiz, separados por ';': ")
indice = numeros.find(';')
radicando = int(numeros[:indice])
#print('Radicando', radicando) # check #
ind_raiz = int(numeros[indice+1:])
#print('Índice da raiz', ind_raiz) # check #
radiciacao = funcao_radiciacao(radicando,ind_raiz) # chamada à função ...
print("A raiz", ind_raiz, "do radicando", radicando, "é: ", radiciacao)  ### Não funciona para radicandos negativos !! Pesquisar motivo. ###

