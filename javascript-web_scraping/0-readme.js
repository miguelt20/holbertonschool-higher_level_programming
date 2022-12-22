#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

fs.readFile(String(args[2]), (err, buff) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(buff.toString());
});
