#!/usr/bin/node

const arg = process.argv;

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

if (isNaN(arg[2]) || isNaN(arg[3]) || process.argv.length < 3) {
  console.log('NaN');
} else {
  add(Number(process.argv[2]), Number(process.argv[3]));
}
