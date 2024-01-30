#!/usr/bin/node
/**
 * Writes a string to a file.
 * @param {string} filename - The filename to write to.
 * @param {string} str - The string to write.
 */

const fs = require("fs");
const file = process.argv[2];
const content = process.argv[3];

fs.writeFile(file, content, "utf8", (err) => {
  if (err) {
    console.error(err);
  }
});
