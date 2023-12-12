#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1 || num === undefined || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const num_ = parseInt(process.argv[2]);

console.log(factorial(num_));
