#!/usr/bin/node
// script that prints all characters of a Star Wars movie

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
      const characters = JSON.parse(body).characters;

      characters.forEach((actorApi) => {
        request(actorApi, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            if (response.statusCode === 200) {
              console.log(JSON.parse(body).name);
            }
          }
        });
      });
    }
  }
});
