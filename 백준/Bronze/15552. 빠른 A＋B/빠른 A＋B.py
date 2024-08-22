import sys  

input = sys.stdin.read 
data = input().splitlines() 

num = int(data[0])
result = []

for i in range(1, num + 1): 
    a, b = map(int, data[i].split()) 
    result.append(str(a + b)) 

sys.stdout.write("\n".join(result) + "\n") 