
N, K = map(int, input().split())

people = list(range(1, N + 1))

result = []

index = 0

while people:
    index = (index + K - 1) % len(people)
    result.append(people.pop(index))

print("<" + ", ".join(map(str, result)) + ">")
