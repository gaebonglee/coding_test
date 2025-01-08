let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim();

let n = Number(input);

for (let i = 1; i <= n; i++) {
    console.log('*'.repeat(i));
}