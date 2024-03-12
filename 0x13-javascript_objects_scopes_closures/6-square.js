#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (character) {
    if (character === undefined) {
      character = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += character;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
