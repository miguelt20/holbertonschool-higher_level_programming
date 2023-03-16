#!/usr/bin/node

const args = process.argv;
const argsLenght = args.length - 2;

if (argsLenght === 0) {
  console.log(0);
} else if (argsLenght === 1) {
  console.log(0);
} else {
  args.sort(function (a, b) { return a - b; });
  const secondLast = parseInt(args[argsLenght]);
  console.log(secondLast);
}
