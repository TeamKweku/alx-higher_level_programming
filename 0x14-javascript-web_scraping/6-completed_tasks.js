#!/usr/bin/node
// Script that computes the number of tasks completed by user ID

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./6-completed_tasks.js <apiUrl>');
  process.exit(1);
}
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasks = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completedTasks[todo.userId]) {
            completedTasks[todo.userId]++;
          } else {
            completedTasks[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasks);
    }
  }
});
