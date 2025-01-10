let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [A, B] = input[0].split(' ').map(Number);

let reverseA = Number(String(A).split('').reverse().join(''));
let reverseB = Number(String(B).split('').reverse().join(''));

if (reverseA > reverseB) {
  console.log(reverseA);
} else {
  console.log(reverseB);
}

