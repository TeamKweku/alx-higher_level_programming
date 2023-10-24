#!/usr/bin/node
// a script that writes a string to a file

const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

const data = process.argv[3];
const filePath = process.argv[2];

// write string to file
fs.writeFile(filePath, data, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
