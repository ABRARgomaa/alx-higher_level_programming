#!/usr/bin/node
const num = process.argv[2];
if (isNaN(parseInt(num))) {
  console.log('Missing size');
} else {
  let line = '';
  const count = parseInt(num);
  for (let i = 0; i < count; i++) {
    for (let j = 0; j < count; j++) {
      line += 'X';
    }
    console.log(line);
    line = '';
  }
}
