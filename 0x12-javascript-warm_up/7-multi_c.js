#!/usr/bin/node
const freq = parseInt(process.argv[2], 10);

if (isNaN(freq)) {
  console.log('Missing number of occurences');
} else {
  for (let index = 0; index < freq; index++) {
    console.log('C is fun');
  }
}
