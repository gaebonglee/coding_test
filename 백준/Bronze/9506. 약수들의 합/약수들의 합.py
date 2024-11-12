while True:
    n = int(input())
    if n == -1:    
        break
        
    divisors = []
    for i in range(1, n):
         if n % i == 0: 
                divisors.append(i)
    total = sum(divisors)
    if total == n:
        print(f"{n} = " + " + ".join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")
        