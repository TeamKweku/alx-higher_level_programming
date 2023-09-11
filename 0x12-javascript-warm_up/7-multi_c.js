#!/usr/bin/node

const args = process.argv.slice(2);

const numValue = Math.floor(Number(args[0]));

if (!isNaN(numValue)) {
  if (numValue <= 0) {
    process.exit();
  }

  for (let i = 0; i < numValue; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
