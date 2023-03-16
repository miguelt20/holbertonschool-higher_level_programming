#!/usr/bin/node

const args = process.argv;
const request = require('request');

const requestURL = `https://swapi-api.hbtn.io/api/films/${args[2]}`;

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
}
request(requestURL, callback);
