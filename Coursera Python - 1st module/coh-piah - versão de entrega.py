### Jan. 18, 2022
### Last Exercise week 09 Coursera Python Phase 01
### COH-PIAH Program - My own version
### Portuguese version - English version will soon be uploaded

### Trabalho de conclusão de curso Python 1ª Etapa - Coursera
### Programa COH-PIAH - Minha própria versão entregue ao final do curso.

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###


################# AQUI SE INICIA A PARTE DO PROGRAMA QUE FOI ENTREGUE PRONTA, A FIM DE SER COMPLEMENTADA ######################

try:
    import re
except:
    print("Falhou em importar módulo 're' ...")
    quit()

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento.
    Já veio definida, não podendo ser alterada !! '''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto: 
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

# Sentenças: trechos do texto separados por ponto (.), exclamação (!) e interrogação (?), de acordo com este programa.
def separa_sentencas(texto): 
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

############### AQUI SE ENCERRA A PARTE DO PROGRAMA QUE FOI ENTREGUE PRONTA ####################


############### A PARTIR DESTE PONTO, COMPETE AO ALUNO IMPLEMENTAR AS ROTINAS SOLICITADAS ########################

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    somatorio = 0
    while i <= 5:
        somatorio = somatorio + abs(as_a[i] - as_b[i])
        i += 1
   
    return somatorio / 6
    
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal_texto = ttr_texto = hlr_texto = sal_texto = sac_texto = pal_texto = 0

    lista_sentencas = separa_sentencas(texto)
    
    lista_lista_frases=[]
    for cadaSentenca in lista_sentencas:
        cadaFrase = separa_frases(cadaSentenca)
        lista_lista_frases.append(cadaFrase)
    
    
    lista_frases = []  # Gera uma lista única com todas as frases, a partir da lista da lista de frases anterior.
    for cadaFrase in lista_lista_frases:
        i = 0
        while i < len(cadaFrase):
            lista_frases.append(cadaFrase[i])
            i+=1
    
    lista_lista_palavras=[]
    for cadaFrase in lista_frases:
        cadaPalavra = separa_palavras(cadaFrase)
        lista_lista_palavras.append(cadaPalavra)
    
    lista_palavras=[]  # Gera uma lista única com todas as palavras a partir da lista da lista de palavras anterior.
    for cadaPalavra in lista_lista_palavras:
        i = 0
        while i < len(cadaPalavra):
            lista_palavras.append(cadaPalavra[i])
            i+=1
    
    # 01) CALCULAR O TAMANHO MÉDIO DE PALAVRA (wal_texto).
    nrTotalPalavras = len(lista_palavras)
    
    tamanhoPalavras = 0
    for cadaPalavra in lista_palavras:
        tamanhoPalavras = tamanhoPalavras + len(cadaPalavra)
    
    wal_texto = tamanhoPalavras / nrTotalPalavras
    
    # 02) CALCULAR A RELAÇÃO TYPE-TOKEN (ttr_texto).
    nrPalavrasDiferentes = n_palavras_diferentes(lista_palavras)
    ttr_texto = nrPalavrasDiferentes / nrTotalPalavras
    
    # 03) CALCULAR A RAZÃO HAPAX LEGOMANA (hlr_texto).
    nrPalavrasUnicas = n_palavras_unicas(lista_palavras)
    hlr_texto = nrPalavrasUnicas / nrTotalPalavras
    
    # 04) CALCULAR O TAMANHO MÉDIO DE SENTENÇA  (sal_texto).
    totalCaractereSentencas = 0
    for cadaSentenca in lista_sentencas:
        totalCaractereSentencas = totalCaractereSentencas + len(cadaSentenca)
    
    sal_texto = totalCaractereSentencas / len(lista_sentencas)
    
    # 05) CALCULAR A COMPLEXIDADE MÉDIA DE SENTENÇA (sac_texto).
    sac_texto = len(lista_frases)/len(lista_sentencas)
    
    # 06) CALCULAR O TAMANHO MÉDIO DE FRASE (pal_texto).
    totalCaractereFrases = 0
    for cadaFrase in lista_frases:
        totalCaractereFrases = totalCaractereFrases + len(cadaFrase)
    pal_texto = totalCaractereFrases / len(lista_frases)
   
    return [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com 
    maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 0
    menor_Sab = None
    while i <= len(textos)-1:
        as_a = calcula_assinatura(textos[i])
        Sab = compara_assinatura(as_a, ass_cp)
        if menor_Sab == None:
            menor_Sab = Sab
            n = 1
        if Sab < menor_Sab:
            menor_Sab = Sab
            n = i + 1
        i += 1
    return n
    

def main():
    as_b = le_assinatura()  
        
    # 01)    
    textos = le_textos()

    # 02)    
    aval = avalia_textos(textos, as_b)  # 'n' deve se referir ao número do texto plagiado

    print("O autor do texto {} está infectado com COH-PIAH".format(aval))

main()

# Texto 01: Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.
# Texto 02: Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.
# Texto 03: Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.
# Texto 04 do teste de assinatura dado no exercício: Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.

