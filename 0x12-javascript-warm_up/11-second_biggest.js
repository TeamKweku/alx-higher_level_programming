#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const numLength = args.length;

if (numLength < 2) {
  console.log(0);
} else {
  let max = 0;
  let minMax = 0;

  for (const num of args) {
    if (num > max) {
      minMax = max;
      max = num;
    } else if (num > minMax && num < max) {
      minMax = num;
    }
  }

  console.log(minMax);
}
