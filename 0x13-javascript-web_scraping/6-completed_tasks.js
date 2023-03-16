#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];

function callback (error, response, body) {
  if (!error || response.statusCode === 200) {
    const data = JSON.parse(body);
    const dic = {};
    for (const d of data) {
      dic[d.userId] = 0;
    }
    for (const d of data) {
      if (d.completed === true) { dic[d.userId] += 1; }
    }
    const copyDic = dic;
    const keys = Object.keys(copyDic);
    for (let i = 1; i <= keys.length; i++) {
      if (copyDic[i] === 0) {
        delete dic[i];
      }
    }
    console.log(dic);
  }
}

request(url, callback);
