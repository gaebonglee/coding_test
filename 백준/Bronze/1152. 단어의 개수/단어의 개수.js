let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim();

let answer = 0;

if (input !== "") {
  answer = input.split(' ').length;
}

console.log(answer);