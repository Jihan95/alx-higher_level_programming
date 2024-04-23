#!/usr/bin/node
const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) { process.stdout.write(c); }
        console.log();
      }
    } else { this.print(); }
  }
}

module.exports = Square;
