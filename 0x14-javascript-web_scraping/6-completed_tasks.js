#!/usr/bin/node
const request = require('request');
const responseBody = {};
const URL = process.argv[2];

request(URL, function (e, resp, body) {
  const todos = JSON.parse(body);
  for (const todo of todos) {
    if (todo.completed) {
      if (todo.userId in responseBody) {
        responseBody[todo.userId]++;
      } else {
        responseBody[todo.userId] = 1;
      }
    }
  }

  console.log(responseBody);
});
