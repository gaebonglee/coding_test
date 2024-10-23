
N, M = map(int, input().split())


A = []
for _ in range(N):
    A.append(list(map(int, input().split())))


B = []
for _ in range(N):
    B.append(list(map(int, input().split())))


C = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    C.append(row)


for row in C:
    print(" ".join(map(str, row)))
