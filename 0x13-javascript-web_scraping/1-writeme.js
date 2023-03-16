#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

fs.writeFile(String(args[2]), String(args[3]), 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
