#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rectangle = '';
      for (let j = 0; j < this.width; j++) {
        rectangle += 'X';
      }
      console.log(rectangle);
    }
  }
};
