n = int(input()) 
people = [] 

for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))


rank = [1] * n  


for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:  # 덩치가 작으면
            rank[i] += 1  

for r in rank:
    print(r, end=' ')
