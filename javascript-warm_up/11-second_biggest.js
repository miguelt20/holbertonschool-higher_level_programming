#!/usr/bin/node

const args = process.argv;
const argsLenght = args.length - 2;

if (argsLenght === 0) {
  console.log(0);
} else if (argsLenght === 1) {
  console.log(0);
} else {
  args.sort();
  const secondLast = parseInt(args[argsLenght]);
  console.log(secondLast);
}
