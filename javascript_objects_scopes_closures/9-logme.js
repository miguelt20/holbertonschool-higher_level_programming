#!/usr/bin/node

let myFuncCalls = 0;

exports.logMe = function (item) {
  myFuncCalls++;
  console.log(`${myFuncCalls}` + ':' + ` ${item}`);
};
