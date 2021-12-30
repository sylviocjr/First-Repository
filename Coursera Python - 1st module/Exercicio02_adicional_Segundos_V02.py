

### Cálculo do resultado em número de "Dias" ###
segundos_totais = input("Por favor, entre com o número de segundos que deseja converter:")
segundos_totais = int(segundos_totais)
dias = segundos_totais//86400
dias = int(dias)
#print(dias,"dias,")

resto = segundos_totais%86400
resto = int(resto)
#print("Resto =",resto)

### Cálculo do resultado em número de "horas" ###
horas = resto//3600
horas = int(horas)
#print(horas, "horas,")

resto = resto%3600
resto = int(resto)
#print("Resto =",resto)

### Cálculo do resultado em número de "minutos" ###
minutos = resto//60
minutos = int(minutos)
#print(minutos, "minutos e")

resto = resto%60
resto = int(resto)
#print("Resto =",resto)

### Cálculo do resultado em número de "segundos" ###
segundos = resto
print(segundos, "segundos.")


print(dias,"dias,",horas, "horas,",minutos, "minutos e", segundos, "segundos.")
