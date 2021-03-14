/*
 * Autor: Marco Antonio Sanchez Hernandez
 * Nacionalidad: Mexicana
 * Fecha de elaboracion: 13-03-2021
 * Ultima modificacion: 14-03-2021
 * Sistema Operativo utilizado: Arch Linux
 * Kernel: Linux 5.11.5-arch1-1
*/

#include <stdio.h>
#include <stdlib.h> //Libreria estandar, contiene la funcion system (const char*string).
#include "show.h" //Liberiria creada, contiene la funcion que muestra en pantalla y actualiza el sudoku.

int main(){

  //Arreglo bidimensional que contiene el sudoku resuelto correctamente.
  int sudoku[9][9] = {4,2,7,  1,3,9,  5,6,8,  9,1,5,  8,7,6,  3,4,2,  6,8,3,  5,4,2,  1,9,7,  2,5,6,  9,1,8,  4,7,3,  3,4,9,  2,6,7,  8,5,1,  8,7,1,  4,5,3,  9,2,6,  5,9,8,  6,2,1,  7,3,4,  7,6,4,  3,8,5,  2,1,9,  1,3,2,  7,9,4,  6,8,5};
  
  //Arreglo bidimensional que contiene las respuestas ingresadas por el usuario.
  int respuestas[9][9] = {4,2,7,  1,0,0,  0,6,8,  0,0,5,  0,0,6,  3,0,0,  6,0,3,  0,0,0,  1,0,0,  2,0,0,  0,1,0,  4,0,0,  3,4,0,  0,6,7,  0,5,1,  8,0,1,  0,5,0,  0,2,0,  0,9,0,  0,0,0,  7,3,0,  7,0,4,  3,0,0,  2,0,9,  0,3,2,  0,9,4,  6,0,0};

  //Variables
  int x, y, z, a = 0, errores = 0, opcion = 0;

  do{
    //Muestra las instrucciones de funcionamiento al usuario.
    printf("\n\t\t*** Sudoku ***\n\n");
    printf("Ingrese tres n\u00FAmeros enteros separados por una coma\n");
    printf("-Deben ser numeros entre 1 y 9, incluyendo el 1 y 9\n");
    printf("-El primer n\u00FAmero corresponde al rengl\u00F3n\n");
    printf("-El segundo n\u00FAmero corresponde a la columna\n");
    printf("-El tercer n\u00FAmero corresponde a su respuesta\n\n");
    mostrar(respuestas); //Muestra en pantalla el sudoku que contiene las respuestas que da el usuario.
    printf("\n\nErrores: %d",errores); //Muestra el numero de errores cometidos.
    printf("\nIngrese su respuesta: ");
    scanf("%d, %d, %d", &x, &y, &z); //Lee de la entrada estandar 3 valores separados por una coma y los almacena en las variables x, y, z.
    
    //Condicion para limitar que los valores enteros ingresados sean mayores que cero, y menores que 10.
    if (x < 1 || x > 9 || y < 1 || y > 9 || z < 1 || z > 9) {
      printf("Los valores ingresados no v\u00E1lidos\n");
      system("read -n 1 -s -p\"Presione cualquier tecla para continuar\""); //Espera a que el usuario presione alguna tecla para continuar con la ejecucion.
    }

    else{
      //Compara si el valor ingresado del usuario es igual al contenido en el arreglo que contiene las respuestas corresctas en la posicion [x][y].
      if (z == sudoku[x-1][y-1]) {
	//Asigna el valor z ingresado por el usuario a la posicion [x-1][y-1] del arreglo que contiene las respuestas del usuario.
	respuestas[x-1][y-1] = z;
	a = 0;

	//Ciclo que realiza la suma de todos los elementos contenidos en el arreglo respuests.
	for (int i = 0; i < 9; i++)
	  for (int j = 0; j < 9; j++)
	    a = a + respuestas[i][j];
      }

      else {
	//Notifica al usuario que cometio un error y espera a que este presione una tecla.
	printf("Error:\n");
	system("read -n 1 -s -p\"Presione cualquier tecla para continuar\""); //Espera a que el usuario presione alguna tecla para reanudar la ejecucion.
	
	//Aumenta el numero de errores.
	errores = errores +1;

	//Si el usuario comete 5 erroes, el programa termina.
	if (errores == 5) {
	  //Asigna el valor 2 a la variable opcion para mostrar un mensaje de derrota.
	  opcion = 2;
	  break;
	}
      }
    }

    system("clear"); //Limpia la pantalla ejecutando un script propio de la terminal de comandos.
  }while( a != 405); //El ciclo se repite hasta que la suma de los elementos del arreglo respuestas sea 405.

  //Permite seleccionar el mensaje final a mostrar.
  switch(opcion) {
    //Este mensaje se muestra si el usuario completa el sudoku correctamente.
    default:
      printf("Enhorabuena, lo lograste\n");
      printf("No. de errores: %d",errores);
    break;

    //Este mensaje se muestra si el usuario cometio 5 errores.
    case 2:
      system("clear"); //Limpia la pantalla ejectunado un script propio de la terminal.
      printf("Intento terminado\n");
      printf("Suerte para la pr\u00F3xima\n\n");
    break;
  }

  return 0;

}
