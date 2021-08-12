'''

Semáforo Epidemiológico COVID-19

Programando por: Marco Antonio Sánchez Hernández
OS utilizado: Manjaro Linux x86_64
Versión de Python: 3.9.6
Versión del programa: 1.1
Última modificación: 12-08-2021

'''


from os import system       #Importar método system del módulo os


#Variables
contador=0          #Contador para el número de personas contagiadas
cont_0_18=0         #Contador para el número de personas contagiadas entre 0 y 18 años
cont_19_29=0        #Contador para el número de personas contagiadas entre 19 y 29 años
cont_30_39=0        #Contador para el número de personas contagiadas entre 30 y 39 años
cont_40_49=0        #Contador para el número de personas contagiadas entre 40 y 49 años
cont_50_59=0        #Contador para el número de personas contagiadas entre 50 y 59 años
cont_60_69=0        #Contador para el número de personas contagiadas entre 60 y 69 años
cont_70_79=0        #Contador para el número de personas contagiadas entre 70 y 79 años
cont_80_89=0        #Contador para el número de personas contagiadas entre 80 y 89 años
cont_90=0           #Contador para el número de personas contagiadas de 90 o más años



'''Recolección de datos'''

base_datos=open("bd.csv", "r")
datos=base_datos.readlines()
base_datos.close()



'''Análisis de datos'''

for i in range(0, len(datos)):
    temp=datos[i].split(',')    #Lista que alamacena la edad y el indicador 
    edad=int(temp[0])           #Se obtiene la edad de la persona
    indicador=float(temp[1])    #Se obtiene el indicador asociado a la misma persona
    
    #Se determina si una persona tiene COVID-19
    if indicador>=0.8:
        contador+=1

        #Se determina la edad de la persona y se clasifica en algún rango de edad
        if (edad>-1 and edad<19):
            cont_0_18+=1
        elif (edad>18 and edad<30):
            cont_19_29+=1
        elif (edad>29 and edad<40):
            cont_30_39+=1
        elif (edad>39 and edad<50):
            cont_40_49+=1
        elif (edad>49 and edad<60):
            cont_50_59+=1
        elif (edad>59 and edad<70):
            cont_60_69+=1
        elif (edad>69 and edad<80):
            cont_70_79+=1
        elif (edad>79 and edad<90):
            cont_80_89+=1
        elif edad>89:
            cont_90+=1

        #Este caso fue añadido con el fin de detectar errores en los datos ingresados
        else:
            print("ERROR: edad fuera de rango")

#Se agrupan en listas el número de personas contagiadas para cada rango de edad
casos=[[cont_0_18, '0-18'],
       [cont_19_29, '19-29'],
       [cont_30_39, '30-39'],
       [cont_40_49, '40-49'],
       [cont_50_59, '50-59'],
       [cont_60_69, '60-69'],
       [cont_70_79, '70-79'],
       [cont_80_89, '80-89'],
       [cont_90, '90 o más']]

#Se ordenan las listas en orden ascendente con el fin de obtener el rango con mayor número de casos
casos.sort()
temp=casos[8]       #Variable que contiene el rango con mayor número de contagios y el número de contagios



'''Interfaz gráfica'''

system("clear")     #Se limpia la terminal en un sistema operativo UNIX/Linux

print("\n\t\t\t\tSemáforo Epidemiológico COVID-19\n")


'''
Se determina el color del semáforo epidemiológico de acuerdo a la variable contador,
además, se muestra el número de personas infectas, el rango edad donde más personas infectadas
se presentan y el número de personas infectadas dentro de dicho rango.
'''

if contador==0:
    print("Color de semáforo epidemiológico: Verde")
    print("No existe alguna persona infectada con el virus SARS-COV 2")
elif contador>0 and contador<=30:
    print("Color de semáforo epidemiológico: Amarillo")
    print("Número de personas infectadas con el virus SARS-COV 2:", contador)
    print("Rango de edad en el cual se presenta el mayor número de contagios: " + str(temp[1]) + " años")
    print("Número de contagios en ese rango de edad: " + str(temp[0]))
elif contador>30 and contador<=70:
    print("Color de semáforo epidemiológico: Naranja")
    print("Número de personas infectadas con el virus SARS-COV 2:", contador)
    print("Rango de edad en el cual se presenta el mayor número de contagios: " + str(temp[1]) + " años")
    print("Número de contagios en ese rango de edad: " + str(temp[0]))
elif contador>70:
    print("Color de semáforo epidemiológico: Rojo")
    print("Número de personas infectadas con el virus SARS-COV 2:", contador)
    print("Rango de edad en el cual se presenta el mayor número de contagios: " + str(temp[1]) + " años")
    print("Número de contagios en ese rango de edad: " + str(temp[0]))
else:
    print("\nERROR: fuera de rango\n")
