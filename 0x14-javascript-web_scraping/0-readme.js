#!/usr/bin/node

fs = require("fs");

fs.readfile(procees.argv[2], "utf-8", (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
