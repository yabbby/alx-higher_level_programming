#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (e, resp, body) {
  const bodyObj = JSON.parse(body);
  let count = 0;
  for (const episode of bodyObj.results) {
    for (const characterUrl of episode.characters) {
      const tmp = characterUrl.split('/');
      const characterId = parseInt(tmp[tmp.length - 2]);
      if (characterId === 18) {
        count++;
      }
    }
  }

  console.log(count);
});
