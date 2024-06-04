#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const completedTasks = {};

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const parsedBody = JSON.parse(body);
  for (let i = 0; i < parsedBody.length; i++) {
    const item = parsedBody[i];
    if (item.completed && completedTasks[item.userId.toString()]) {
      completedTasks[item.userId.toString()] += 1;
    } else if (item.completed) {
      completedTasks[item.userId.toString()] = 1;
    }
  }
  console.log(completedTasks);
});
