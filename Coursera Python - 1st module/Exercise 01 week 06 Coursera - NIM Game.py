### Dec. 20, 2021 ###
### Exercise for Coursera Python week 6 ###
### Key words: NIM game; functions; Python functions ###
### This program runs the NIM game ###

### Palavras-chave: Jogo de NIM; funções; funções em Python ###
### Este programa executa o Jogo de NIM ###

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###



pontoParaComputador = 0 ### Inicialização das variáveis globais que serão manipuladas na f. partida() ###
pontoParaUsuario = 0



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
    if n % (m+1) == 0:
        print("\nVocê começa!\n")
############################################## ALTERNÂNCIA #################################
        while n > 0:
            pecas_retiradas_usuario = usuario_escolhe_jogada(n,m)
            if pecas_retiradas_usuario == 1:
                print("\nVocê tirou uma peça.")
            
            else:
                print("\nVocê tirou",pecas_retiradas_usuario, "peças.")

            n = n - pecas_retiradas_usuario
            print("Agora restam",n,"peças no tabuleiro.\n")

            if n == 0:
                pontoParaUsuario += 1
                print("Fim do jogo! Você ganhou!\n\n")
                #print(pontoParaUsuario,"ponto(s) para você !!")   ### Somente para verificação. Eliminar ao final ###

      ### ROTINA COMPUTADOR CONTINUA ###  
        
            pecas_retiradas_computador = computador_escolhe_jogada(n,m)
            if pecas_retiradas_computador == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", pecas_retiradas_computador, "peças.")
            n = n - pecas_retiradas_computador
            print("Agora restam",n,"peças no tabuleiro.\n")
            if n == 0:
                pontoParaComputador += 1
                print("Fim do jogo! O computador ganhou!\n\n")
                #print(pontoParaComputador,"ponto(s) para o computador !!")   ### Somente para verificação. Eliminar ao final ###
        
###################################### FIM  DE ALTERNÂNCIA ###################################

    ### ROTINA COMPUTADOR COMEÇA ###
    else:
        print("\nComputador começa!\n")
        
    while n > 0:
        pecas_retiradas_computador = computador_escolhe_jogada(n,m)
        if pecas_retiradas_computador == 1:
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou", pecas_retiradas_computador, "peças.")   ### Reposicionar posteriormente cf. necessidade ###
        n = n - pecas_retiradas_computador
        print("Agora restam",n,"peças no tabuleiro.\n")
        if n == 0:
            pontoParaComputador += 1
            print("Fim do jogo! O computador ganhou!\n\n")
            #print(pontoParaComputador,"ponto(s) para o computador !!")   ### Somente para verificação. Eliminar ao final ###
            break   ### Interrompe caso o fim de jogo tenha ocorrido neste ponto, impedindo que o usuário continue. ###
############################################## ALTERNÂNCIA #################################

    ### ROTINA USUÁRIO CONTINUA ####

        pecas_retiradas_usuario = usuario_escolhe_jogada(n,m)
        if pecas_retiradas_usuario == 1:
            print("\nVocê tirou uma peça.")
        else:
            print("\nVocê tirou",pecas_retiradas_usuario, "peças.")

        n = n - pecas_retiradas_usuario
        print("Agora restam",n,"peças no tabuleiro.\n")

        if n == 0:
            pontoParaUsuario += 1
            print("Fim do jogo! Você ganhou!\n\n")
            #print(pontoParaUsuario,"ponto(s) para você !!")   ### Somente para verificação. Eliminar ao final ###        

        

def campeonato():   ### Chama a função partida() 3 vezes ###
    n = 1
    while n <= 3:   
        print("**** Rodada", n, "****", end = "\n\n")
        partida()
        n += 1
    #if pontoParaComputador > pontoParaUsuario:
        #print("Fim do jogo! O computador ganhou !", end = "\n")
    #else:
        #print("Fim do jogo! Você ganhou !", end = "\n")
    print("**** Final do campeonato! ****", end = "\n\n")
    print("Placar: Você", pontoParaUsuario, "X", pontoParaComputador, "Computador")
    
    
def main():

    while True:
        try:    ### ROTINA DE VALIDAÇÃO NA ESCOLHA ENTRE PARTIDA/CAMPEONATO ###
    
            print("Bem-vindo ao jogo do NIM! Escolha:", end = "\n")
            print("1 - para jogar uma partida isolada")
            print("2 - para jogar um campeonato")
            opcao = int(input())   ### Observar este comando !!! ###
            if opcao == 1:   
                print("Você escolheu uma partida isolada!\n\n")
                partida()   ### Uma única chamada à função partida() ###
                break
            if opcao == 2:
                print("Você escolheu um campeonato!\n\n")
                campeonato()
                break
        except:
            continue   ### Retorna ao início do loop ###

def usuario_escolhe_jogada(a,b):
    retirar = 0   # Força entrada no loop a seguir ...
    while retirar <=0 or retirar > b:
        retirar = int(input("Quantas peças você vai retirar? "))
        if retirar <=0 or retirar > b:   ### Rotina de validação ###
            print("Oops! Jogada inválida! Tente de novo.\n\n")
    return retirar


def computador_escolhe_jogada(a,b):   ### Não necessita validação !!! ###
    retirar = 1
    while retirar <= b:
        if (a-retirar)% (b+1) == 0:
            break
        retirar += 1
    return retirar               

main()


