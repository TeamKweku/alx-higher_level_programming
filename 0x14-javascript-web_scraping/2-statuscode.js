#!/usr/bin/node
// a script that display the status code of a GET request

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./2-statuscode.js <url_path>');
  process.exit(1);
}

const urlPath = process.argv[2];

request(urlPath, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
