class Stack {
  constructor(){
    this.nodes = [];
  }

  function IsEmpty() {
    return this.nodes.length == 0;
  }

  function push_node(node) {
    this.nodes.push(node);
  }

  function pop_node() {
    if (IsEmpty()) {
      console.log("Underflow");
    } else {
      return this.nodes.pop();
    }
  }

  funtion peek_node() {
    return this.nodes[this.nodes.length - 1];
  }

}
