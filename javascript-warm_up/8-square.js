#!/usr/bin/node

const arg = process.argv;

if (isNaN(arg[2]) || !arg[2]) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg[2]; i++) {
    let square = '';
    for (let j = 0; j < arg[2]; j++) {
      square += 'x';
    }
    console.log(square);
  }
}
