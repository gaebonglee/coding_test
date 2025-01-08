let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [hour, minute] = input[0].split(' ').map(Number)
let plusTime = Number(input[1])

let totalMinute = hour*60 + minute + plusTime
totalMinute %= 1440;
hour = Math.floor(totalMinute / 60);
minute = totalMinute % 60

console.log(hour + ' ' + minute)