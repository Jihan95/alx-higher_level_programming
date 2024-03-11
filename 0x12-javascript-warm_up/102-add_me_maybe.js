#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  return 1 + theFunction(number);
}
module.exports = { addMeMaybe };
