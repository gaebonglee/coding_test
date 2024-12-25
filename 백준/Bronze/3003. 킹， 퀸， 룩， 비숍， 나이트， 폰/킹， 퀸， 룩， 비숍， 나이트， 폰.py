correct_pieces = [1, 1, 2, 2, 2, 8]
current_pieces = list(map(int, input().split()))

result = [correct_pieces[i] - current_pieces[i] for i in range(6)]
print(" ".join(map(str, result)))
