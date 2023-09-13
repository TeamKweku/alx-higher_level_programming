#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./102-concat.js fileA fileB fileC');
  process.exit();
}

const [file1, file2, file3] = process.argv.slice(2);

const fileA = fs.readFileSync(file1, 'utf8');
const fileB = fs.readFileSync(file2, 'utf8');
const fileC = fileA + fileB;

fs.writeFileSync(file3, fileC);
