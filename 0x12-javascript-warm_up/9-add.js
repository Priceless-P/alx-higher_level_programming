#!/usr/bin/node

function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  return sum;
}
const args = process.argv;
const a = args[2];
const b = args[3];

console.log(add(a, b));
