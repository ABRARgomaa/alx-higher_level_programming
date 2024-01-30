#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const num1 = process.argv[2];
const num2 = process.argv[3];
if (isNaN(parseInt(num1)) | isNaN(parseInt(num2))) {
  console.log(NaN);
} else {
  const n1 = parseInt(num1);
  const n2 = parseInt(num2);
  console.log(add(n1, n2));
}
