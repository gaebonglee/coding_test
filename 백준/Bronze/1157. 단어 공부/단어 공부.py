
word = input().upper()
alphabet_count ={}

for char in word:
    if char in alphabet_count:
        alphabet_count[char]+=1
    else:
        alphabet_count[char]=1

max_count = max(alphabet_count.values())
most_common = [char for char, count in alphabet_count.items() if count == max_count]
if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])