let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let N = Number(input[0]);
let words = input.slice(1);

let groupWordCount = 0;

for (let word of words) {
  let seen = new Set();
  let isGroupWord = true;
  let prevChar = '';

  for (let char of word) {
    if (seen.has(char) && char !== prevChar) {
      isGroupWord = false;
      break;
    }
    seen.add(char);
    prevChar = char;
  }

  if (isGroupWord) {
    groupWordCount++;
  }
}

console.log(groupWordCount);
