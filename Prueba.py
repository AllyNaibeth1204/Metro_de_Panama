import pandas as pd 
#import os
#print(os.getcwd())
data = pd.read_csv("c:/Users/ISABEL/Documents/Ing. sistema computacional/Samsung Innovation Campus/Prueba de pandas/METRO_DE_PANAMA.csv", encoding="latin1", sep=";")
#print(csv)

df = pd.DataFrame(data)

""" funcion para agregar la columna monto final y al mismo tiempo reemplazar todos los signos a nada y solo dejar los numeros y junto 
que sume los valores de las 4 columnas fila por fila 
"""
df['monto_final'] = df.apply(lambda row: sum(float(row.iloc[i].replace('B/.', '').replace(',', '').replace('-', '0')) for i in [3, 5, 7, 9]), axis=1)

#print(df['monto_final'])
#primero buscamos el maximo luego la fila donde lo encontramos y terminamos buscando el mes con la fila 
mes_maximo = df['monto_final'].max()
fila_mes_maximo = df[df['monto_final'] == mes_maximo]
fecha_mes_maximo = fila_mes_maximo['ï»¿FECHA'].values[0]
print(f"Mes con mayor Ganancia es {fecha_mes_maximo} con el monto de: {round(mes_maximo, 2)}")

mes_minimo = df['monto_final'].min()
fila_mes_minimo = df[df['monto_final'] == mes_minimo]
fecha_mes_minimo = fila_mes_minimo['ï»¿FECHA'].values[0]
print(f"Mes con menor Ganancia es {fecha_mes_minimo} con el monto de: {round(mes_minimo, 2)}")

#Pasasejros maximos y minimos 
df['PASAJEROS MENSUAL'] = df['PASAJEROS MENSUAL'].str.replace(',', '').str.replace('-', '0').astype(float)
mes_maximo_pasajeros = df['PASAJEROS MENSUAL'].max()
fila_mes_maximo_pasajeros = df[df['PASAJEROS MENSUAL'] == mes_maximo_pasajeros]
fecha_mes_maximo_pasajeros = fila_mes_maximo_pasajeros['ï»¿FECHA'].values[0]
print(f"Mes con mayor numero de usuarios es {fecha_mes_maximo_pasajeros} con la cantidad de: {round(mes_maximo_pasajeros, 0)}")

mes_minimo_pasajeros = df['PASAJEROS MENSUAL'].min()
fila_mes_minimo_pasajeros = df[df['PASAJEROS MENSUAL'] == mes_minimo_pasajeros]
fecha_mes_minimo_pasajeros = fila_mes_minimo_pasajeros['ï»¿FECHA'].values[0]
print(f"Mes con menor numero de usuarios es {fecha_mes_minimo_pasajeros} con el cantidad de: {round(mes_minimo_pasajeros, 0)}")

#estudiantes maximos 
df['Estudiantes'] = df['Estudiantes'].str.replace(',', '').str.replace('-', '0').astype(float)
mes_maximo_estudiantes = df['Estudiantes'].max()
fila_mes_maximo_estudiantes = df[df['Estudiantes'] == mes_maximo_estudiantes]
fecha_mes_maximo_estudiantes = fila_mes_maximo_estudiantes['ï»¿FECHA'].values[0]
print(f"Mes con mayor numero de usuarios estudiantes es {fecha_mes_maximo_estudiantes} con la cantidad de: {round(mes_maximo_estudiantes, 0)}")

#Media pasajeros
media_pasajeros = df['PASAJEROS MENSUAL'].mean()
print("La media de pasajeros es: ", round(media_pasajeros, 0))

#Dinero Mensual 
Dinero_mensual = df.groupby['monto_final'].sum()
print("Ganancia mensual: ", Dinero_mensual)

#Dinero anual 
df['Año'] = df['ï»¿FECHA'].dt.year

monto_anual = df.groupby('Año')['monto_final'].sum()
print("Dinero anual del monto total:")
print(monto_anual)