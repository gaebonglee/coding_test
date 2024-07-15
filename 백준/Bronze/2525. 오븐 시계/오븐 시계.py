A, B = map(int, input().split())
C = int(input())

total_minutes = A * 60 + B
total_minutes += C

new_A = (total_minutes // 60) % 24
new_B = total_minutes % 60

print(new_A, new_B)