#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const PATH = process.argv[3];

request(URL, function (e, resp, body) {
  fs.writeFileSync(PATH, body, {
    encoding: 'utf-8'
  });
});
