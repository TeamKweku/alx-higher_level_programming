#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const result = number + 1;

  theFunction(result);
};
