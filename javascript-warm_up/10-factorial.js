#!/usr/bin/node

const arg = process.argv;

function factorialize (num) {
  if (!num) { return 1; } else if (num < 0) { return -1; } else if (num == 0) { return 1; } else {
    return (num * factorialize(num - 1));
  }
}

console.log(factorialize(arg[2]));
