#!/usr/bin/node
/**
 * Gets the contents of a webpage and stores it in a file.
 * @param {string} str - URL to request
 * @param {string} str - file path to store the body response
 */

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, data) => {
  if (err) {
    console.error(err);
  } else {
    data = data.body;
    fs.writeFile(filePath, data, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
