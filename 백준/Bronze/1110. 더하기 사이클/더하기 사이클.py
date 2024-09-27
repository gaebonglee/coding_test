N = int(input())
originalNum = N
count = 0

while True:
    count+=1
    N = (N % 10) * 10 + (N // 10 + N % 10) % 10

    if N == originalNum:
        break

print(count)