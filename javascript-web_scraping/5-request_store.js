#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const filename = String(args[3]);

function callback (error, response, body) {
  if (!error || response.statusCode === 200) {
    const data = JSON.stringify(body);
    fs.writeFile(filename, JSON.parse(data), 'utf-8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
}

request(url, callback);
