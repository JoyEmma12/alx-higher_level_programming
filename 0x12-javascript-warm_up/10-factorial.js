#!/usr/bin/node

const n = parseInt(process.argv[2]);

function fact (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }

  return n * fact(n - 1);
}

console.log(fact(n));
