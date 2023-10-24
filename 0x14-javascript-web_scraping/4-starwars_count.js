#!/usr/bin/node
// script that prints the number of movies where
// the character “Wedge Antilles” is present
const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./3-starwars_title.js <id>');
  process.exit(1);
}

const url = process.argv[2];
// const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const count = body.split('/people/18/').length - 1;
    console.log(count);
    // if (response.statusCode === 200) {
    //   const movies = JSON.parse(body).results;
    //   const match = movies.filter((movie) => movie.characters.includes(character));
    //   console.log(match.length);
    // }
  }
});
