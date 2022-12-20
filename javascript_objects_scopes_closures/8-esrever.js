#!/usr/bin/node

exports.esrever = function (list) {
  const listLength = list.length;
  const reverseList = [];
  for (let i = (listLength - 1); i >= 0; i--) {
    reverseList.push(list[i]);
  }
  return reverseList;
};
