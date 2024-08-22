X = int(input())
N = int(input())

total = 0

for _ in range (N):
    price, quantity = map(int, input().split())
    total += price * quantity

if total == X :
    print("Yes")
else : 
    print("No")