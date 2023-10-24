#!/usr/bin/node
// a script that reads and prints the content of a file

const fs = require('fs');

if (process.argv.length < 3) {
  console.log('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read content of file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
