#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  let j = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    reversed[i] = list[j];
    j--;
  }
  return reversed;
};
