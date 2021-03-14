/*
 * Autor: Marco Antonio Sanchez Hernandez
 * Nacionalidad: Mexicana
 * Fecha de elaboracion: 13-03-2021
 * Ultima modificacion: 14-03-2021
 * Sistema Operativo utilizado: Arch Linux
 * Kernel: Linux 5.11.5-arch1-1
*/

/*Definicion de la funcion mostrar
-Recibe como parametro un arreglo bidimensional de 9x9 de numeros enteros.
-No regresa ningun valor.
*/
void mostrar(int arreglo[9][9]) {

  //Variables de iteracion
  int i, j;

  /*Bloque de codigo que permite imprimir el sudoku con el formato deseado*/
  printf("\n");
  for (i = 0; i < 9; i++) {
    //Imprime una linea punteada cada tres lineas para separar los renglones.
    if (i == 3 || i ==6)
      printf("\t      -------------------\n");
    printf("\t      "); //Inserta una tabulacion y 6 espacios antes de imprimir los numeros.
    for (j = 0; j < 9; j++) {
      //Imprime una barra vertical cada tres numeros.
      if (j == 3 || j == 6)
	printf("|%d",arreglo[i][j]);
      else {
	printf(" %d",arreglo[i][j]);
      }
    }
    printf("\n");
  }

}
