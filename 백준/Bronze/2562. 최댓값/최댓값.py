numbers = [int(input()) for _ in range(9)] 
maxNum = max(numbers)  
index = numbers.index(maxNum) + 1

print(maxNum)  # 최댓값 출력
print(index)