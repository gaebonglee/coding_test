def hotel(h, w, n):
    floor = n % h
    room = (n // h) + 1

    if floor == 0:
        floor = h
        room -= 1

    return f"{floor}{room:02d}"

t = int(input()) 
for _ in range(t):
    h, w, n = map(int, input().split())
    print(hotel(h, w, n))