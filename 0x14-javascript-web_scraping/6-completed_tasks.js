#!/usr/bin/node
/**
 * Computes the number of tasks completed by user id
 * @param {string} str - API URL: https://jsonplaceholder.typicode.com/todos
 */

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(response.body);
    const usersCompletedTasks = {};
    tasks.forEach(task => {
      if (task.completed) {
        if (usersCompletedTasks[task.userId]) {
          usersCompletedTasks[task.userId]++;
        } else {
          usersCompletedTasks[task.userId] = 1;
        }
      }
    });
    console.log(usersCompletedTasks);
  }
});
