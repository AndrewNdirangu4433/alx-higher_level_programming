#!/usr/bin/node

const printOut = 'C is fun';

const arg = process.argv;

if (isNaN(arg[2]) || process.argv.length < 2) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < arg[2]; a++) {
    console.log(printOut);
  }
}
