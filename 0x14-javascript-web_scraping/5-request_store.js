#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Usage: ./5-request_store.js <url> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  }
});
