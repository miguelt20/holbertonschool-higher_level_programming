#!/usr/bin/node

let myFuncCalls = 0 - 1;

exports.logMe = function (item) {
  myFuncCalls += 1;
  console.log(`${myFuncCalls}` + ':' + ` ${item}`);
};
