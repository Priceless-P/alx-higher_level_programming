#!/usr/bin/node

const args = process.argv;
const toNum = parseInt(args[2]);
if (!isNaN(toNum)) {
  console.log('My number: ' + toNum);
} else {
  console.log('Not a number');
}
