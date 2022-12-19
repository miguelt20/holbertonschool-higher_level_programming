#!/usr/bin/node

import process from 'process';

const arg = process.argv;

if (!isNaN(arg[2])) {
  const newVal = parseInt(arg[2]);
  console.log('My number: ' + newVal);
} else {
  console.log('Not a number');
}
