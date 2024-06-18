#!/usr/bin/node

const arg = process.argv;

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length > 2) {
  console.log(arg[2]);
}
