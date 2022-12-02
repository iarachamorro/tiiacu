print("ingrese dias")
dias = int(input())
print("ingrese horas")
horas = int(input())
print("ingrese minutos")
minutos = int(input())
print("ingrese segundos")
segundos = int(input())

dias_segundos = dias*86400
horas_segundos = horas*3600
minutos_segundos = minutos*60

segundos_totales= segundos+dias_segundos+horas_segundos+minutos_segundos
print(segundos_totales)




                                                                                                        