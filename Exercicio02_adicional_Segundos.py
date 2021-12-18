

# Necessário aperfeiçoar !!

segundos_totais = input("Por favor, entre com o número de segundos que deseja converter:")
segundos_totais = int(segundos_totais)
dias = segundos_totais//86400
dias = int(dias)
#print(dias,"Dias")
horas = (segundos_totais%86400)/3600
horas = int(horas)
#print(horas, "horas")
minutos = (segundos_totais%86400)%3600/60
minutos = int(minutos)
#print(minutos, "minutos")
segundos = ((segundos_totais%86400)%3600)%60
#print(segundos, "segundos")
print(dias,"dias,",horas, "horas,",minutos, "minutos e", segundos, "segundos.")
