#!/usr/bin/node

const args = process.argv.slice(2);

const numValue = Math.floor(Number(args[0]));

if (!isNaN(numValue)) {
  console.log(`My number: ${numValue}`);
} else {
  console.log('Not a number');
}
