'''
Jan 31, 2022.
This program is intended to be used only for my own instructional purposes of Operational Research
as a student of Mathematics Bachelor degree @ Unisul (Brazil).
'''
'''
Esta versão retorna o maior lucro possível, dadas as variáveis e seus limites, a partir de randomização
das variáveis e um certo número de simulações, definida pelo usuário.'''

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

import random

simulacoes = int(input("Número de simulações: "))
maior_lucro = 0
for i in range(simulacoes):
    QA = random.randint(200, 390)
    QB = random.randint(20, 33)
    QC = random.randint(15, 20)
    QD = random.randint(30, 46)
    QE = random.randint(6, 11)
    
    lucro = 4.47*QA + 5.36*QB + 6.70*QC + 5.81*QD + 6.26*QE
    restricao_couro = 0.13*QA + 0.14*QB + 0.19*QC + 0.17*QD + 0.18*QE
    restricao_couraca = 0.032*QA + 0.0377*QB + 0.0489*QC + 0.0413*QD + 0.0443*QE
    restricao_tempo = 7.5*QA + 15*QB + 15*QC + 15*QD + 15*QE
    if (lucro >= maior_lucro) and (restricao_couro <= 390) and (restricao_couraca <= 96) and (restricao_tempo <= 3200):
        maior_lucro = lucro
        QA_melhor = QA
        QB_melhor = QB
        QC_melhor = QC
        QD_melhor = QD
        QE_melhor = QE


print("Lucro: $$ {:.2f}".format(maior_lucro))
print("Variáveis: QA(390) = {}, QB(33) = {}, QC(20) = {}, QD(46) = {}, QE(11) = {}.".format(QA_melhor, QB_melhor,
QC_melhor, QD_melhor, QE_melhor))
#print("Restrição de couro(390): {:.2f}".format(restricao_couro))
#print("Restrição de couraça(96): {:.2f}".format(restricao_couraca))
#print("Restrição de tempo(3200): ", restricao_tempo)

print("\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")