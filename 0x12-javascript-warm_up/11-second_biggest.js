#!/usr/bin/node
function sorts (args) {
  const numbers = args.slice(2).map(Number);
  const sorted = numbers.sort((a, b) => b - a);
  if (sorted.length >= 2) {
    return sorted[1];
  } else {
    return 0;
  }
}
console.log(sorts(process.argv));
