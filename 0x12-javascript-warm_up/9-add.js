#!/usr/bin/node
const num1 = process.argv[2];
const num2 = process.argv[3];
if (!isNaN(num1) && !isNaN(num2)) add(parseInt(num1), parseInt(num2));
else console.log('NaN');
function add (a, b) {
  console.log(a + b);
}
