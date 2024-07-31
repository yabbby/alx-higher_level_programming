#!/usr/bin/node
const request = require('request');

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  function (e, resp, body) {
    const bodyObj = JSON.parse(body);
    console.log(bodyObj.title);
  }
);
