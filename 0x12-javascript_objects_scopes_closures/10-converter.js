#!/usr/bin/node

exports.converter = function (base) {
  function convert (nb) {
    return nb.toString(base);
  }
  return convert;
};
