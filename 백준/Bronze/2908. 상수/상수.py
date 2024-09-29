a, b = map(int, input().split())

strA = str(a)
strB = str(b)

listA = list(strA)
listB = list(strB)

listA.reverse()
listB.reverse()

resultA = int("".join(listA))
resultB = int("".join(listB))

if listA > listB:
   print(resultA)
else:
   print(resultB)


