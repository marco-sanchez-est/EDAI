/*
 * Autor: Marco Antonio Sanchez Hernandez
 * Nacionalidad: Mexicana
 * Fecha de elaboracion: 11-03-2021
 * Ultima modificacion: 14-03-2021
 * Sistema Operativo utilizado: Arch Linux
 * Kernel: Linux 5.11.5-arch1-1
 *
*/

#include <stdio.h>
#include <stdlib.h> //Libreria estandar, contiene la funcion int system(const char*string).
#include <string.h> //Liberia string, contiene la funcion strcpy que permite limpiar un arreglo.
#include "mensaje.h" //Libreria creada, contiene las funciones para cifrar y descifrar un mensaje.

int main() {

  //Variables.
  unsigned short opcion = 0;
  int ren, col; //Almacenan el tamanio de la escitala.
  char mensaje[ren*col]; //Almacena el mensaje que se desea cifrar o descifrar.

  do{
    system("clear"); //Limpia la pantalla ejecutando el script clear propio de la terminal.
    opcion = ren = col = 0; //Inicia el valor de las variables en cero.
    strcpy(mensaje,"\0"); //Limpia el arreglo mensaje. 

    //Menu de opciones.
    printf("\n\t*** ES\u00CDTALA ESPARTANA ***\n");
    printf("\u00BFQu\u00E9 desea realizar?\n");
    printf("1) Crear mensaje cifrado.\n");
    printf("2) Descifrar mensaje.\n");
    printf("3) Salir.\n\n");
    scanf("%hu", &opcion); //Leer opcion ingresada.

    switch(opcion) {
      case 1:
	printf("\nIngrese el tama\u00F1o de la escitala:\n");
	printf("\nRenglones: ");
	scanf("%d",&ren);

	//No permite ingresar valores negativos.
	if (ren < 1) {
	  printf("El valor ingresado no es v\u00E1lido\n");
	  break;
	}

	printf("Columnas: ");
	scanf("%d",&col);

	//No permite ingresar valores negativos.
	if (col < 1) {
	  printf("El valor ingresado no es v\u00E1lido\n");
	  break;
	}

	printf("\nEscriba el texto a cifrar:\n");
	scanf("%s",mensaje);
	cifrar(ren,col,mensaje); //Pasa los argumentos ren, col y mensaje a la funcion cifrar
	system("read -n 1 -s -p\"\nPresione cualquier tecla para continuar\""); //Espera a que el usuario presione alguna tecla para reanudar la ejecucion.
      break;

      case 2:
	printf("\nIngrese el tama\u00F1o de la escitala:\n");
	printf("\nRenglones: ");
	scanf("%d",&ren);

	//No permite ingresar valores negativos.
	if (ren < 1) {
	  printf("El valor ingresado no es v\u00E1lido\n");
	  break;
	}

	printf("Columnas: ");
	scanf("%d",&col);

	//No permite ingresar valores negativos.
	if (col < 1) {
	  printf("El valor ingresado no es v\u00E1lido\n");
	  break;
	}

	printf("\nEscriba el texto a descifrar:\n");
	scanf("%s",mensaje);
	descifrar(ren,col,mensaje); //Pasa los argumentos ren, col y mensaje a la funcion descifrar
	system("read -n 1 -s -p\"\nPresione cualquier tecla para continuar\""); //Espera a que el usuario presione alguna tecla para reanudar la ejecucion.
      break;

      case 3:
	return 0; //Termina la ejecucion de la funcion main, y por tanto, del programa.

      default:
	printf("Opci\u00F3n no v\u00E1lida.\n");
	system("read -n 1 -s -p\"\nPresione cualquier tecla para continuar\""); //Espera a que el usuario presione alguna tecla para reanudar la ejecucion.
      break;

    }
  }while(opcion != 3);

  return 0;

}
