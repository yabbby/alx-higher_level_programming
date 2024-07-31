#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (e, resp, body) {
  console.log(`code: ${resp && resp.statusCode}`);
});
