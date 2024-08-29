N = [int(input()) for _ in range(10)]
M = [num%42 for num in N]
unique_M = set(M)
print(len(unique_M))