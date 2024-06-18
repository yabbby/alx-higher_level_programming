#!/usr/bin/node
const nums = process.argv;

if (nums.length <= 3) {
  console.log(0);
} else {
  nums.splice(0, 2);
  nums.sort();
  console.log(nums[nums.length - 2]);
}
