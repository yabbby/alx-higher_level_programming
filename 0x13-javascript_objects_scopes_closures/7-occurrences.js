#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let count = 0;
  list.forEach(el => {
    if (el === searchElement) { count++; }
  });

  return count;
}

module.exports = { nbOccurences };
