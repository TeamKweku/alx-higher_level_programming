#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];

  const listSize = list.length;

  for (let i = listSize - 1; i >= 0; i--) {
    revList.push(list[i]);
  }

  return revList;
};
