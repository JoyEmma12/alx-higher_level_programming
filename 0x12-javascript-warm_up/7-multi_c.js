#!/usr/bin/node

const par = parseInt(process.argv[2]);

if (par) {
  for (let i = 0; i < par; ++i) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
