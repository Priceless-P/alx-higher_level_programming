#!/usr/bin/node
/**
 * Reads and prints the content of a file.
 * @param {string} file - The file to read.
 */

const fs = require("fs");
const file = process.argv[2];

fs.readFile(file, "utf8", (err, data) => {
  if (data) {
    console.log(data);
    return;
  }
  if (err) {
    console.log(err);
  }
});
