n = int(input())
for _ in range(n):
    quiz_result = input()
    score = 0
    consecutive_score = 0

    for char in quiz_result:
        if char == 'O':
            consecutive_score+=1
            score += consecutive_score
        else:
            consecutive_score = 0

    print(score)