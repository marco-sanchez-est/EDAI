/*  En este documento se definen las funciones de cada botón de la calculadora */


/*En cada función se obtiene la cadena de caracteres contenida en el elemento p con el id operation,
  el cual se encuentra definido en la división display, con excepción de la última función, todas las
  funciones concatenan el carácter correspondiente a la cadena.*/

//Elimina toda la cadena anteriormente escrita
function clear_display() {
  document.getElementById("operation").textContent = '';
}


//Escribe un paréntesis abierto (, actualmente no es utilizada en la calculadora
function print_open() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '(';
}


//Escribe un paréntesis cerrado ), actualmente no es utilizada en la calculadora
function print_close() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + ')';
}


//Escribe el número cero
function print_0(str) {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '0';
}


//Escribe el número 1
function print_1() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '1';
}


//Escribe el número 2
function print_2() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '2';
}


//Escribe el número 3
function print_3() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '3';
}


//Escribe el número 4
function print_4() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '4';
}


//Escribe el número 5
function print_5() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '5';
}


//Escribe el número 6
function print_6() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '6';
}


//Escribe el número 7
function print_7() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '7';
}


//Escribe el número 8
function print_8() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '8';
}


//Escribe el número 9
function print_9() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '9';
}


//Escribe el signo más
function print_plus() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '+';
}


//Escribe el signo menos
function print_minus() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '-';
}


//Escribe el signo de multiplicación (*)
function print_times() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '*';
}


//Escribe el signo de división (/)
function print_division() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '/';
}


//Escribe el símbolo de potencia (^), actualmente no es usada en la calculadora
function print_power() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '^';
}


//Escribe una representación del símbolo de raiz cuadrada, actualmente no es usada en la calculadora
function print_square() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + 'v';
}


//Permite eliminar un carácter de la cadena ingresada
function delete_char() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp.slice(0, temp.length - 1);
}
