testCase = int(input())  

for _ in range(testCase):
    floor = int(input())  
    unit = int(input())  


    people = [i for i in range(1, unit + 1)] 
    for f in range(1, floor + 1): 
        for u in range(1, unit):
            people[u] += people[u - 1]
    
    print(people[-1]) 