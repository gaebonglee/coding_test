let fs = require('fs'); 
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let N = parseInt(input[0]);

let numbers = input[1].split(' ').map(Number);

let min = Math.min(...numbers);
let max = Math.max(...numbers);

console.log(`${min} ${max}`);




