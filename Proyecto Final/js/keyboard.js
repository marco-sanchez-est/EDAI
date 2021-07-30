function clear_display() {
  document.getElementById("operation").textContent = '';
}

function print_open() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '(';
}

function print_close() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + ')';
}

function print_0(str) {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '0';
}

function print_1() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '1';
}

function print_2() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '2';
}

function print_3() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '3';
}

function print_4() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '4';
}

function print_5() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '5';
}

function print_6() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '6';
}

function print_7() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '7';
}

function print_8() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '8';
}

function print_9() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '9';
}

function print_plus() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '+';
}

function print_minus() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '-';
}

function print_times() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '*';
}

function print_division() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '/';
}

function print_power() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + '^';
}

function print_square() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp + 'v';
}

function delete_char() {
  var temp = document.getElementById("operation").textContent;
  document.getElementById("operation").textContent = temp.slice(0, temp.length - 1);
}
