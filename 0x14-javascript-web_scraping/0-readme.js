#!/usr/bin/node
const fs = require('fs');

try {
  const contents = fs.readFileSync(process.argv[2], {
    encoding: 'utf-8'
  });
  console.log(contents);
} catch (e) {
  console.log(e);
}
