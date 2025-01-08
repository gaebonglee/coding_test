let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let testCase = Number(input[0]);
let answer = '';

for (let t = 1; t <= testCase; t++) {
    let [a, b] = input[t].split(' ').map(Number);
    answer += (a + b) + '\n';
}

console.log(answer);