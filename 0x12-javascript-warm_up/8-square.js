#!/usr/bin/node

const args = process.argv;

if (args.length >= 2) {
  const numOccurrences = Number(args[2]);
  if (!isNaN(numOccurrences) && numOccurrences >= 1) {
    let i = 0;
    while (i < numOccurrences) {
      console.log('X'.repeat(numOccurrences));
      i++;
    }
  } else if (!isNaN(numOccurrences) && numOccurrences < 1) {
    process.exit();
  } else {
    console.log('Missing size');
  }
}
