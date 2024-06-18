#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

const firstNum = parseInt(process.argv[2], 10);
console.log(factorial(firstNum));
