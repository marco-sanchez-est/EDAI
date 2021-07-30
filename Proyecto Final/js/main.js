class Stack {
  constructor(){
    this.nodes = [];
  }

  IsEmpty() {
    return this.nodes.length == 0;
  }

  push_node(node) {
    this.nodes.push(node);
  }

  pop_node() {
    if (IsEmpty()) {
      console.log("Underflow");
    } else {
      return this.nodes.pop();
    }
  }

  peek_node() {
    return this.nodes[this.nodes.length - 1];
  }

}


function calculate() {
  var temp = new Stack();
  let str = document.getElementById("operation").textContent;
  const infix = str.split("");
  var postfix = [];
  for (var i = 0; i < infix.length; i++) {
    if (infix[i] < 48 || infix[i] > 57) {
      postfix.push(infix[i]);
    } else {
      temp.push_node(infix[i]);
    }
  }
  document.getElementById("operation").textContent = postfix.join(" ");
}
