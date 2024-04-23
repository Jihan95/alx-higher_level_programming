#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  return theFunction(1 + number);
}
module.exports = { addMeMaybe };
