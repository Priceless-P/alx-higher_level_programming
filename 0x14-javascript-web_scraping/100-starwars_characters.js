#!/usr/local/bin/node
/**
 * Prints all characters of a Star Wars movie
 * @param {string} str - the movie ID
 */

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    response = JSON.parse(response.body);
    for (let i = 0; i < response.characters.length; i++) {
      request.get(response.characters[i], (err, response) => {
        if (err) {
          console.error(err);
        } else {
          const characterResponse = JSON.parse(response.body);
          console.log(characterResponse.name);
        }
      });
    }
  }
});
