#!/usr/bin/python3

# Autor: Marco Antonio Sanchez Hernandez
# Nacionalidad: mexicana
# Fecha de elaboracion: 19-03-2021
# Ultima modificacion: 19-03-2021
# Sistema Operativo utilizado: Arch Linux
# Kernel: 5.11.5-arch1-1
# NOTA: Compatible con Windows 10, solo se debe eliminar la primera linea del archivo.

#Importar unicamente la funcion system y name del modulo os.
from os import system, name

#Variables globales.
option = 0
alfabetoLatino = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


#Funcion que convierte una lista en una cadena de caracteres.
def listToString(list):
    cadena = "" 
    return (cadena.join(list)) #Une cada elemento contenido en una lista en una cadena de caracteres.


#Funcion que reordena el alfabeto de acuerdo con el valor de la variable entera llave.
def alfabetos(llave):
    global alfabetoCifrado #Se declara como una variable global.
    alfabetoCifrado = [] #Arreglo vacio que contendra el nuevo abecedario.

    for i in range(26):
        alfabetoCifrado.append(alfabetoLatino[llave]) #Aniade un nuevo elemento al arreglo alfabetoCifrado.
        llave = llave + 1

        if (llave > 25):
            llave = 0

    return None


#Funcion para cifrar un mensaje.
def cifrar():
    array2 = [] #Arreglo vacio que contendra el mensaje cifrado.

    #Limita la entrada del usuario a solo numeros enteros.
    try:
        llave = int(input("Ingrese un n\u00FAmero entero del 1 al 25: "))
    except ValueError: #Si el usuario ingresa otro valor que no sea un numero entero se ejecuta este bloque.
        print("\nIngresar un n\u00FAmero entero")
        print("Presione ENTER para continuar")
        input() #Espera que el usuario presione ENTER o ingrese algun valor para continuar.
        return None #Se termina anticipadamente la funcion y se regresa al menu principal.

    if (llave < 1 or llave > 25):
        print("\nEl valor ingresado no es v\u00E1lido")
        print("Presione ENTER para continuar")
        input() #Espera que el usuario presione ENTER o ingrese algun valor para continuar.

    #Este bloque de codigo se ejectura si el valor de llave esta entre 1 y 25.
    else:
        alfabetos(llave) #Pasa el valor de la variable llave a la funcion alfabetos
        mensaje = str(input("Ingrese el mensaje que desea cifrar: "))
        array1 = list(mensaje.upper()) #Convierte la cadena de caracteres ingresada en un arreglo de letras mayusculas.
    
        for i in range(len(array1)):
            j = 0
         
            #Busca la posicion que ocupa una letra en alfabetoLatino.
            while (array1[i] != alfabetoLatino[j]):
                j = j + 1

            array2.append(alfabetoCifrado[j]) #Aniade un nuevo elemento al arreglo array2.

        mensajeCifrado = listToString(array2) #Convierte el arreglo array2 en una cadena de caracteres.
        print(mensajeCifrado)
        print("\nPresione ENTER para continuar")
        input() #Espera a que el usuario presione ENTER o ingrese algun valor.

    return None


#Funcion para descifrar un mensaje.
def descifrar():

    array2 = [] #Arreglo vacio que contendra el mensaje descifrado.

    #Limita la entrada del usuario a solo numeros enteros.
    try:
        llave = int(input("Ingrese un n\u00FAmero entero del 1 al 25: "))
    except ValueError: #Si el usuario ingresa otro valor que no sea un numero entero se ejecuta este bloque.
        print("\nIngresar un n\u00FAmero entero")
        print("Presione ENTER para continuar")
        input() #Espera que el usuario presione ENTER o ingrese algun valor para continuar.
        return None #Se termina anticipadamente la funcion y se regresa al menu principal.

    if (llave < 1 or llave > 25):
        print("\nEL valor ingresado no es v\u00E1lido")
        print("Presione ENTER para continuar\n")
        input() #Espera que el usuario presione ENTER o ingrese algun valor para continuar.

    else:
        alfabetos(llave)
        mensaje = str(input("Ingrese el mensaje que desea descifrar: "))
        array1 = list(mensaje.upper()) #Convierte la cadena de caracteres ingresada en un arreglo de letras mayusculas.

        for i in range(len(array1)):
            j = 0

            #Busca la posicion que ocupa una letra en alfabetoCifrado.
            while (array1[i] != alfabetoCifrado[j]):
                j = j +1

            array2.append(alfabetoLatino[j]) #Aniade un nuevo elemento al arreglo array2.

        mensajeDescifrado = listToString(array2) #Convierte el arreglo array2 en una cadena de caracteres.
        print(mensajeDescifrado)
        print("\nPresione ENTER para continuar")
        input() #Espera que el usuario presione ENTER o ingrese algun valor para continuar.

    return None


#Ciclo principal
while option != 3:

    option = 0

    #Llamada a scripts para limpiar la terminal.
    if name == 'nt':
        _ = system('cls') #Script para Windows 10.

    else:
        _ = system('clear') #Script para MacOS y Linux.

    #Muestra el menu de opciones
    print("\n\tCifrado C\u00E9sar\n")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Salir\n")

    #Limita la entrada del usuario a solo numeros enteros.
    try:
        option = int(input("Seleccione una opci\u00F3n: "))
    except ValueError: #Si el usuario ingresa otro valor que no sea un numero entero se ejecuta este bloque.
        print("\nIngresar un n\u00FAmero entero")

    #Default
    if (option < 1 or option > 3):
        print("\nEL valor ingresado no es v\u00E1lido")
        print("Presione ENTER para continuar")
        input() #Espera que el usuario presione ENTER o ingrese algun valor para continuar.

    #Case 1
    elif (option == 1):
        cifrar() #Llama a la funcion cifrar

    #Case 2
    elif (option == 2):
        descifrar() #Llama a la funcion descifrar
