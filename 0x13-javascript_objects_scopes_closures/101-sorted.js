#!/usr/bin/node
const dict = require('./101-data').dict;

const userIdOccurence = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (!userIdOccurence[occurrence]) {
    userIdOccurence[occurrence] = [];
  }

  userIdOccurence[occurrence].push(userId);
}

console.log(userIdOccurence);
