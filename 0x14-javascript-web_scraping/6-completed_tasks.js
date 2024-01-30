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
    const res = JSON.parse(response.body);
    const userIds = [];
    for (let i = 0; i < res.length; i++) {
      userIds.push(res[i].userId);
    }

    const uniqueUserIds = new Set(userIds);
    const completedSum = [];
    const usersCompletedTasks = {};

    for (const uniqueUserId of uniqueUserIds) {
      let userCompleted = 0;
      for (let i = 0; i < res.length; i++) {
        if (uniqueUserId === res[i].userId) {
          if (res[i].completed) {
            userCompleted++;
          }
        }
      }
      completedSum.push(userCompleted);
    }
    uniqueUserIds.forEach((key, index) => {
      usersCompletedTasks[key] = completedSum[index - 1];
    });
    console.log(usersCompletedTasks);
  }
});
