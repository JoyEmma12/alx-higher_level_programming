#!/usr/bin/node

const par = parseInt(process.argv[2]);

if (par) {
  for (let i = 0; i < par; ++i) {
    let x = 0;

    while (x < par) {
      process.stdout.write('X');
      ++x;
    }

    if (x === par) {
      console.log('');
    }
  }
} else {
  console.log('Missing size');
}
