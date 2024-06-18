#!/usr/bin/node

const arg = process.argv;

if (isNaN(arg[2]) || process.argv.length < 2) {
  console.log('Missing size');
} else {
  for (let a = 0; a < arg[2]; a++) {
    console.log('X'.repeat(arg[2]));
  }
}
