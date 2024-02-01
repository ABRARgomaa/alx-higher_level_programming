#!/usr/bin/node

const hi = require('./5-square.js');

class Square extends hi {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let line = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        line += c || 'X';
      }
      console.log(line);
      line = '';
    }
  }
}

module.exports = Square;
