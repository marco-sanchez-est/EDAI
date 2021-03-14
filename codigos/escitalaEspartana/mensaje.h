/*
 * Autor: Marco Antonio Sanchez Hernandez
 * Nacionalidad: Mexicana
 * Fecha de elaboracion: 11-03-2021
 * Ultima modificacion: 14-03-2021
 * Sistema Operativo utilizado: Arch Linux
 * Kernel: Linux 5.11.5-arch1-1
 *
*/

/* Definicion de la funcion cifrar, recibe como parametros:
 * Dos valores enteros.
 * Un arreglo de caracteres que tenga por tamanio el producto de los valores enteros.
 * No retorna valor alguno. */
void cifrar(int ren, int col, char texto[ren*col]) {

  // Variables locales.
  int i, j, k = 0; // Variables de iteracion.
  char str[ren][col]; /* Arreglo bidimensional de caracteres, tiene por tamanio los
			 valores enteros que recibe como parametro la funcion*/

  //Ciclo para convertir un arreglo unidimensional en uno bidimensional.
  for (i = 0; i < ren ; i++)
    for (j = 0; j < col; j++)
      str[i][j] = texto[k++];
    //Almacena el valor contenido en el indice k, en el indice i,j del arreglo bidimensional.

  printf("\nEl texto en la tira queda de la siguiente manera:\n");

  //Ciclo para mostrar en pantalla la cadena de caracteres cifrada.
  //Imprime caracter a caracter.
  for (i = 0; i < col; i++)
    for (j = 0; j < ren; j++)
      printf("%c",str[j][i]);

  printf("\n");

}

/* Definicion de la funcion descifrar, recibe como parametros:
 * Dos valores enteros.
 * Un arreglo de caracteres que tenga por tamanio el producto de los valores enteros.
 * No retorna valor alguno. */
void descifrar(int ren, int col, char texto[ren*col]) {

  //Variables.
  int i, j, k = 0; // Variables de iteracion.
  char str[ren][col]; /* Arreglo bidimensional de caracteres, tiene por tamanio los
			 valores enteros que recibe como parametro la funcion.*/

  //Ciclo para convertir un arreglo unidimensional en uno bidimensional.
  for (i = 0; i < col; i++)
    for (j = 0; j < ren; j++)
      str[j][i] = texto[k++];
    //Almacena el valor contenido en el indice k, en el indice j,i del arreglo bidimensional.

  printf("\nEl texto descifrado es:\n");

  //Ciclo para mostrar en pantalla la cadena de caracteres descifrada.
  //Imprime caracter a caracter.
  for (i = 0; i < ren; i++)
    for (j = 0; j < col; j++)
      printf("%c",str[i][j]);

  printf("\n");

}
