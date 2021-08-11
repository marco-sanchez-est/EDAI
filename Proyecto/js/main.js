//Definición de la clase Stack, la cual permite crear una pila
class Stack {

  //Se inicia una pila en un arreglo vacío llamado nodes
  constructor(){
    this.nodes = [];
  }

  //Función que permite determinar si una pila está vacía o no, regreseará verdadero en caso de estar vacía
  IsEmpty() {
    return this.nodes.length == 0;
  }

  //Función que permite insertar un nuevo nodo en la pila, recibe como parámetro el nodo
  push_node(node) {
    this.nodes.push(node); //Regresa un arreglo con el nodo ingresado como último elemento
  }

  //Función que permite eliminar un nodo de la pila, siempre y cuando esta no esté vacía
  pop_node() {
    if (this.IsEmpty()) {
      console.log("Underflow"); //Mensaje mostrado en caso de realizarse la función pop_node en una pila vacía
    } else {
      return this.nodes.pop(); //Regresa un arreglo sin el último elemento
    }
  }

  //Función que permite consultar el elemento tope de la pila
  peek_node() {
    return this.nodes[this.nodes.length - 1]; //Regresa el último elemento ingresado al arreglo
  }

}


//Función que convierte la expresión contenida en el elemento p con id operation en notación polaca inversa
function calculate() {
  var temp = new Stack(); //Se crea una nueva pila temporal
  let str = document.getElementById("operation").textContent; //Se obtiene la cadena de caracteres a convertir
  const infix = str.split(""); //Se separa en caracteres independientes
  var postfix = []; //Variable que almacenará la cadena en notación polaca inversa

  //Conversión a notación polaca inversa
  for (var i = 0; i < infix.length; i++) {

    //Si el carácter infix[i] es un número, este es añadido directamente a la variable postfix
    if (infix[i] < 48 || infix[i] > 57) {
      postfix.push(infix[i]);
    } else { //En caso contrario se procede con alguno de los siguientes casos

      //Si la pila temp está vacía entonces se ingresa el operador a la pila
      if (temp.IsEmpty()) {
        temp.push_node(infix[i]);
      } else if (highpreced(temp.peek_node(), infix[i])) { //Cuando el tope de la pila contiene un operador de menor jerarquía
          temp.push_node(infix[i]); //Se ingresa el operador a la pila
      } else if (highpreced(infix[i], temp.peek_node())) { //Cuando el tope de la pila contiene un operador de mayor jerarquía
          postfix.push(temp.peek_node()); //Se añade el operador contenido en el tope de la pila a la variable postfix
          temp.pop_node(); //Se elimina el elemento tope de la pila
          temp.push_node(infix[i]); //Se ingresa el operador con el que fue comparado el tope de la pila
      } else { //Si el operador es de la misma jerarquía se realiza lo siguiente:
          postfix.push(temp.peek_node()); //Se añade el operador contenido en el tope de la pila a la variable postfix
          temp.pop_node(); //Se elimina el elemento tope de la pila
          temp.push_node(infix[i]); //Se ingresa el operador con el que fue comparado el tope de la pila
      }
    }
  }
    //Se añaden a la cadena los operadores restantes en la pila
    while (!(temp.IsEmpty())) {
      postfix.push(temp.peek_node());
      temp.pop_node();
    }
  //Se muestra la cadena escrita en notación polaca inversa
  document.getElementById("operation").textContent = postfix.join(" ");
}


//Función que permite determinar la jerarquía de una operación
function highpreced(op1, op2) {
  if ((op1 == '+' || op1 == '-') && (op2 == '*' || op2 == '/')) {
    return 1; //Regresará verdadero si op1 es de menor jerarquía que op2
  } else {
    return 0;
  }
}
