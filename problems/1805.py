A, B = map(int, input().split())
print(int(((A + B) * len(range(A, B+1))) / 2))
