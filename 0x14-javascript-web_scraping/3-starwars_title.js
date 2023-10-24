#!/usr/bin/node
// a script that prints the title of a Star Wars
// movie where the episode number matches a given integer.

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./3-starwars_title.js <id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    }
  }
});
