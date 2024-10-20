
canvas = [[0] * 100 for _ in range(100)]


n = int(input())


for _ in range(n):
    x, y = map(int, input().split())
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1 


total_area = 0
for i in range(100):
    for j in range(100):
        if canvas[i][j] == 1:
            total_area += 1


print(total_area)
