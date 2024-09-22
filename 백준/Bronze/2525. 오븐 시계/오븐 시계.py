A, B = map(int, input().split())
C = int(input())

total_minutes = B + C

A += total_minutes // 60  
B = total_minutes % 60 

A %= 24

print(A, B)
