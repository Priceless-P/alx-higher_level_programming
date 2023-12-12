#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    } else {
      return this;
    }
  }

  print() {
    for (let index = 0; index < this.height; index++) {
      console.log("X".repeat(this.width));
    }
  }
}
module.exports = Rectangle;
