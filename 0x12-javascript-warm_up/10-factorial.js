#!/usr/bin/node

const args = process.argv.slice(2);
const num = Math.floor(Number(args[0]));

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return (1);
  } else if (n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(num));
