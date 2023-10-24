#!/usr/bin/node

const request = require('request');

function getMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Unexpected status code: ${response.statusCode}`));
      } else {
        const characters = JSON.parse(body).characters;
        resolve(characters);
      }
    });
  });
}

function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Unexpected status code: ${response.statusCode}`));
      } else {
        const name = JSON.parse(body).name;
        resolve(name);
      }
    });
  });
}

async function printMovieCharacters (movieId) {
  try {
    const characterUrls = await getMovieCharacters(movieId);
    const characterNames = await Promise.all(characterUrls.map(getCharacterName));
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}

if (process.argv.length < 3) {
  console.log('Usage: ./3-starwars_title.js <id>');
  process.exit(1);
}

printMovieCharacters(process.argv[2]);
