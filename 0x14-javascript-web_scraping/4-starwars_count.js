#!/usr/bin/node
/**
 * Prints the number of movies
 * where the character “Wedge Antilles” is present.
 * @param {string} str - API URL of the Star wars
 * API: https://swapi-api.alx-tools.com/api/films/
 */

const request = require("request");
const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    const res = JSON.parse(response.body);
    const results = res.results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const character = results[i].characters;
      for (let j = 0; j < character.length; j++) {
        if (character[j].includes("18")) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
