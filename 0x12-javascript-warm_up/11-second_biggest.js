#!/usr/bin/node

const args = process.argv.slice(2);
const numArray = [];
if (args.length > 2) {
  args.forEach((arg) => {
    numArray.push(parseInt(arg));
  });
  numArray.sort((a, b) => b - a);
  console.log(numArray[1]);
} else {
  console.log(0);
}
