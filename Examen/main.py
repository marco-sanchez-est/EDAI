'''

Semáforo Epidemiológico COVID-19

Programando por: Marco Antonio Sánchez Hernández
OS utilizado: Manjaro Linux x86_64
Versión de Python: 3.9.6
Versión del programa: 1.0
Última modificación: 07-08-2021

'''


from os import system       #Importar método system del módulo os
from re import findall      #Importar método findall del módulo re


#Variables
contador=0          #Contador para el número de personas contagiadas
contador_edad=0     #Contador para la edad de las personas contagiadas


#Recolección de datos
base_datos=open("bd.csv", "r")
datos=base_datos.readlines()
base_datos.close()


#Análisis de datos
for i in range(0, len(datos)):
    temp=findall(r'[\d\.\d]+', datos[i])    #Lista que alamacena la edad y el indicador 
    indicador=float(temp[1])
    edad=int(temp[0])
    
    #Se determina si una persona tiene COVID-19
    if indicador>=0.8:
        contador+=1
        contador_edad=contador_edad+edad


system("clear")     #Se limpia la terminal en un sistema operativo UNIX/Linux
print("\n\t\t\t\tSemáforo Epidemiológico COVID-19\n")


'''
Se determina el color del semáforo epidemiológico de acuerdo a la variable contador,
además, se muestra el número de personas infectas y se calcula la edad promedio de
las personas contagiadas, haciendo uso de la fórmula contador_edad/contador
'''

if contador==0:
    print("Color de semáforo epidemiológico: Verde")
    print("El número de personas infectadas con el virus SARS-COV 2 es 0")
elif contador>0 and contador<=30:
    print("Color de semáforo epidemiológico: Amarillo")
    print("Número de personas infectadas con el virus SARS-COV 2:", contador)
    print("\nEdad promedio: " + str("{:.2f}".format(contador_edad/contador)) + " años\n")
elif contador>30 and contador<=70:
    print("Color de semáforo epidemiológico: Naranja")
    print("Número de personas infectadas con el virus SARS-COV 2:", contador)
    print("\nEdad promedio: " + str("{:.2f}".format(contador_edad/contador)) + " años\n")
elif contador>70:
    print("Color de semáforo epidemiológico: Rojo")
    print("Número de personas infectadas con el virus SARS-COV 2:", contador)
    print("\nEdad promedio: " + str("{:.2f}".format(contador_edad/contador)) + " años\n")
else:
    print("\nERROR: fuera de rango\n")
