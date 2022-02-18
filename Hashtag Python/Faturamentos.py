'''
Jan 26, 2022
Lists homework Hashtag Course - lists

Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.

'''


meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
'outubro', 'novembro', 'dezembro']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

lista_anual = vendas_1sem + vendas_2sem
#print(lista_anual)
#print(len(meses))
#print(len(lista_anual))
#print(min(lista_anual))
#print(max(lista_anual))
faturamento_anual = sum(lista_anual)
i = lista_anual.index(min(lista_anual))
#print(i)

j = lista_anual.index(max(lista_anual))
#print(j)

print('\nO melhor mês do ano foi {}, com R$ {:.2f} de faturamento.'. format((meses[j]), (lista_anual[j])))
print('\nO pior mês do ano foi {}, com R$ {:.2f} de faturamento.'. format((meses[i]), (lista_anual[i])))
print('\nO faturamento total do ano foi R$ {:.2f}.'.format(faturamento_anual))
print('\nO mês de {} representou {:.2%} do faturamento total.'.format(meses[j], lista_anual[j]/faturamento_anual))

# Top 3 !!!

copia_lista_anual = lista_anual.copy()  ''' Preserva a lista original. Observar a forma de copiar a lista.
Não basta somente atribuir igualdade !!! '''

#print('Cópia da lista: ', copia_lista_anual)
top3 = []

cont = 1
while cont <= 3:
    maior_valor = max(copia_lista_anual)
    top3.append(maior_valor)
    copia_lista_anual.remove(max(copia_lista_anual))
    cont += 1

print('\nTop 3 de vendas: R$ {:.2f}, R$ {:.2f} e R$ {:.2f}.'.format(top3[0], top3[1], top3[2]))

print('\nSylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil.\n\n')
