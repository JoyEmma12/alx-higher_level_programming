#!/usr/bin/node

const fs = require('fs');


fs.get(process.argv[2]).on('response', function  (response) {
  console.log(`code: ${response.statusCode}`);
});
