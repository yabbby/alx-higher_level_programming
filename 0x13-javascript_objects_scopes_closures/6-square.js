#!/usr/bin/node

const SuperSquare = require('./5-square.js');

class Square extends SuperSquare {
  charPrint (c) {
    let char = 'X';
    if (c !== undefined) {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
