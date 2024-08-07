#!/usr/bin/node
const fs = require('fs');

try {
  fs.writeFileSync(process.argv[2], process.argv[3], {
    encoding: 'utf-8'
  });
} catch (e) {
  console.log(e);
}
