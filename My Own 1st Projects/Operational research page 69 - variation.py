'''
Jan 31, 2022.
This program is intended to be used only for my own instructional purposes of Operational Research
as a student of Mathematics Bachelor degree @ Unisul (Brazil).
'''

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

import random
tentativas = 0
while True:
    QA = random.randint(200, 390)
    QB = random.randint(20, 33)
    QC = random.randint(15, 20)
    QD = random.randint(30, 46)
    QE = random.randint(6, 11)
    tentativas += 1

    lucro = 4.47*QA + 5.36*QB + 6.70*QC + 5.81*QD + 6.26*QE
    restricao_couro = 0.13*QA + 0.14*QB + 0.19*QC + 0.17*QD + 0.18*QE
    restricao_couraca = 0.032*QA + 0.0377*QB + 0.0489*QC + 0.0413*QD + 0.0443*QE
    restricao_tempo = 7.5*QA + 15*QB + 15*QC + 15*QD + 15*QE
    if (lucro >= 1689.04) and (restricao_couro <= 390) and (restricao_couraca <= 96) and (restricao_tempo <= 3200):
        break
# Valor máximo encontrado foi R$ 1689.04 (Excel Solver)

print("Lucro: $$ {:.2f}".format(lucro))
print("Variáveis: QA(390) = {}, QB(33) = {}, QC(20) = {}, QD(46) = {}, QE(11) = {}.".format(QA, QB, QC, QD, QE))
print("Restrição de couro(390): {:.2f}".format(restricao_couro))
print("Restrição de couraça(96): {:.2f}".format(restricao_couraca))
print("Restrição de tempo(3200): ", restricao_tempo)
print("Número de tentativas: ", tentativas)
print("\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil")