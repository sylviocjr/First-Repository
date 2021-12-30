### Dec. 26, 2021 ###
### Exercise for Coursera week 6 ###
### Key words: NIM game; functions; Python functions ###
### This program runs the NIM game using random inputs ###

### Palavras-chave: Jogo de NIM; funções; funções em Python ###
### Este programa executa o Jogo de NIM usando entradas aleatórias ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###




def partida():

    global pontoParaComputador   ### Lição aprendida a duras penas !!!
    global pontoParaUsuario      ### Necessário avisar Python que estas variáveis são globais,
                                        ### permitindo a sua manipulação dentro da função. ###
    while True:
    ### n: nr peças dispostas sobre o tabuleiro ###
    ### m: nr peças que podem ser movidas a cada jogada ###
        try:
            while True:
                n = int(input("Quantas peças? "))
                if n <=1:   ### Define como n = 2 o número mínimo de peças para o jogo ###
                    print("Entrada inválida! Mínimo 2 peças! Informe novamente ...")
                else:
                    break
            while True:
                m = int(input("Limite de peças por jogada? "))
                if m <=0 or m > n:
                    print("Entrada inválida! Informe novamente ...")
                else:
                    break
            break    
                            
        except:
            continue

    ### ROTINA USUÁRIO COMEÇA ###
    if quemComeca == 1:
        print("Você começa!")
############################################## ALTERNÂNCIA #################################
        while n > 0:
            pecas_retiradas_usuario = usuario_escolhe_jogada(n,m)
            if pecas_retiradas_usuario == 1:
                print("Você tirou uma peça.")
            
            else:
                print("Você tirou",pecas_retiradas_usuario, "peças.")

            n = n - pecas_retiradas_usuario
            print("Agora restam",n,"peças no tabuleiro.")

            if n == 0:
                pontoParaUsuario += 1
                print("Você ganhou!")
                print(pontoParaUsuario,"ponto(s) para você !!")   ### Somente para verificação. Eliminar ao final ###
                break   ### Interrompe caso o fim de jogo tenha ocorrido neste ponto, impedindo que o usuário continue. ###

      ### ROTINA COMPUTADOR CONTINUA ###  
        
            pecas_retiradas_computador = computador_escolhe_jogada(n,m)
            if pecas_retiradas_computador == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", pecas_retiradas_computador, "peças.")
            n = n - pecas_retiradas_computador
            print("Agora restam",n,"peças no tabuleiro.")
            if n == 0:
                pontoParaComputador += 1
                print("O computador ganhou!")
                print(pontoParaComputador,"ponto(s) para o computador !!")   ### Somente para verificação. Eliminar ao final ###
                break   ### Interrompe caso o fim de jogo tenha ocorrido neste ponto, impedindo que o usuário continue. ###
        
###################################### FIM  DE ALTERNÂNCIA ###################################

    ### ROTINA COMPUTADOR COMEÇA ###
    if quemComeca == 2:
        print("")
        
    while n > 0:
        pecas_retiradas_computador = computador_escolhe_jogada(n,m)
        if pecas_retiradas_computador == 1:
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou", pecas_retiradas_computador, "peças.")   ### Reposicionar posteriormente cf. necessidade ###
        n = n - pecas_retiradas_computador
        print("Agora restam",n,"peças no tabuleiro.")
        if n == 0:
            pontoParaComputador += 1
            print("O computador ganhou!")
            print(pontoParaComputador,"ponto(s) para o computador !!")   ### Somente para verificação. Eliminar ao final ###
            break   ### Interrompe caso o fim de jogo tenha ocorrido neste ponto, impedindo que o usuário continue. ###
############################################## ALTERNÂNCIA #################################

    ### ROTINA USUÁRIO CONTINUA ####

        pecas_retiradas_usuario = usuario_escolhe_jogada(n,m)
        if pecas_retiradas_usuario == 1:
            print("Você tirou uma peça.")
        else:
            print("Você tirou",pecas_retiradas_usuario, "peças.")

        n = n - pecas_retiradas_usuario
        print("Agora restam",n,"peças no tabuleiro.")

        if n == 0:
            pontoParaUsuario += 1
            print("Você ganhou!")
            print(pontoParaUsuario,"ponto(s) para você !!")   ### Somente para verificação. Eliminar ao final ###
            break   ### Interrompe caso o fim de jogo tenha ocorrido neste ponto, impedindo que o usuário continue. ###

        

def campeonato():   ### Chama a função partida() 3 vezes ###
    if quemComeca == 1:
        print("Você inicia ... boa sorte !!!")
    if quemComeca == 2:
        print("Computador inicia ...")
    if quemComeca != 1 and quemComeca != 2:
        print("Deu pau rsrsrs !!! ...")   ### Previsto para jamais ocorrer ###

    n = 1
    while n <= 3:   
        print("**** Rodada", n, "****", end = "\n")
        partida()
        n += 1
    if pontoParaComputador > pontoParaUsuario:
        print("Fim do jogo! O computador ganhou !", end = "\n")
    else:
        print("Fim do jogo! Você ganhou !", end = "\n")
    print("**** Final do campeonato! ****", end = "\n")
    print("Placar: Você", pontoParaUsuario, "X", pontoParaComputador, "Computador")
      
    
    

def usuario_escolhe_jogada(a,b):
    retirar = 0   # Força entrada no loop a seguir ...
    while retirar <=0 or retirar > b:
        retirar = int(input("Quantas peças você vai retirar? "))
        if retirar <=0 or retirar > b:   ### Rotina de validação ###
            print("Oops! Jogada inválida! Tente de novo.")
    return retirar


def computador_escolhe_jogada(a,b):   ### Não necessita validação !!! ###
    retirar = 0   # Força entrada no loop a seguir ...
    while retirar <=0 or retirar > b:
        retirar = int(input("Quantas peças o computador vai retirar? "))
        if retirar <=0 or retirar > b:   ### Rotina de validação ###
            print("Oops! Jogada inválida! Tente de novo.")
    return retirar               


import random
pontoParaComputador = 0 ### Inicialização das variáveis globais que serão manipuladas na f. partida() ###
pontoParaUsuario = 0
while True:
    try:    ### ROTINA DE VALIDAÇÃO NA ESCOLHA ENTRE QUEM INICIA O JOGO ###
    
        print("Bem-vindo ao jogo do NIM - 3 Rodadas! Escolha:", end = "\n")
        print("1 - Jogador inicia")
        print("2 - Computador inicia")
        print("3 - Início aleatório")
        opcao = int(input())   ### Observar este comando !!! ###
        if opcao == 1:
            quemComeca = 1   ### Jogador ###
            
            
        elif opcao == 2:
            quemComeca = 2   ### Computador ###
            
            
        elif opcao == 3:
            quemComeca = random.randint(1,2)   ### Seleciona aleatoriamente entre jogador e computador ###
            print("Início aleatório ...")

        else:
            continue  ### Retorna ao início do loop ###
                    
        
    except:
        continue   ### Retorna ao início do loop ###

    #if quemComeca == 1:
        #print("Você inicia ... boa sorte !")
    #if quemComeca == 2:
        #print("Computador inicia ...")
    #if quemComeca != 1 and quemComeca != 2:
        #print("Deu pau rsrsrs !!! ...")   ### Previsto para jamais ocorrer ###

    campeonato()


