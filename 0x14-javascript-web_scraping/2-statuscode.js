#!/usr/bin/node

const fs = require('fs');

arg1 = process.argv[2];

fs.get(arg1).on('response', (response) => {
  console.log("code: ${response.statusCode}");
});
