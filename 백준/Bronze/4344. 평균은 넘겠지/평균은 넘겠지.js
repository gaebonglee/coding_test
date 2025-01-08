let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let C = Number(input[0]); // 테스트 케이스 수

for (let i = 1; i <= C; i++) {
    let scores = input[i].split(' ').map(Number);
    let N = scores[0]; // 학생 수
    let studentScores = scores.slice(1); // 점수 배열

    let avg = studentScores.reduce((a, b) => a + b) / N; // 평균 계산
    let aboveAvg = studentScores.filter(score => score > avg).length; // 평균 초과 학생 수
    let percentage = ((aboveAvg / N) * 100).toFixed(3); // 비율 계산 및 소수점 고정

    console.log(`${percentage}%`);
}