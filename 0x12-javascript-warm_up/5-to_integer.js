#!/usr/bin/node

const par = parseInt(process.argv[2]);

if (par) {
  console.log('My number: ' + par);
} else {
  console.log('Not a number');
}
