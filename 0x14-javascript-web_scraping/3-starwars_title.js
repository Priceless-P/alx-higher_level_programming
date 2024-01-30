#!/usr/bin/node
/**
 * Prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 * @param {string} str - the movie ID
 */

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    const res = JSON.parse(response.body);
    console.log(res.title);
  }
});
