let fs = require('fs'); 
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let numbers=input.map(Number)

let max = Math.max(...numbers)
let maxIndex = numbers.indexOf(max)+1

console.log(max)
console.log(maxIndex)