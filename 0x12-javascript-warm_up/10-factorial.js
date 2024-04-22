#!/usr/bin/node
const num = process.argv[2];
if (!isNaN(num)) {
  const result = factorial(parseInt(num));
  console.log(result);
} else console.log(1);
function factorial (n) {
  if (n === 1) return 1;
  else return n * factorial(n - 1);
}
