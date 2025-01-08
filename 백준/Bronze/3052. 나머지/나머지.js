let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let numbers = input.map(Number);

let remainders = new Set();

for (let i = 0; i < numbers.length; i++) {
    remainders.add(numbers[i] % 42);
}

console.log(remainders.size);