#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

myObject.incr = function () {
  this.value += 1;
  return this;
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
