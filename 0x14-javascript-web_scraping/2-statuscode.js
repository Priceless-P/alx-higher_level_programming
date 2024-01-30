#!/usr/bin/node
/**
 * Display the status code of a GET request.
 * @param {string} str - URL to request (GET)
 */

const request = require('request');
const url = process.argv[2];

request.get(url, (_, response) => {
  {
    console.log('code: ', response.statusCode);
  }
});
