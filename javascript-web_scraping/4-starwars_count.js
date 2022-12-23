#!/usr/bin/node
const args = process.argv;
const request = require('request');

const url = args[2];
const wedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    for (const item of data.results) {
      for (const i of item.characters) {
        if (i === wedgeAntilles) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
}
request(url, callback);
