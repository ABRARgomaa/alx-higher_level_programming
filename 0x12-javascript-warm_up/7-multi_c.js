#!/usr/bin/node
const num = process.argv[2];
if (isNaN(parseInt(num))) {
  console.log('Missing number of occurrences');
} else {
  const count = parseInt(num);
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
