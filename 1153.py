N = int(input())
fator = 0
for i in range(N-1, 0, -1):
    if i == N-1:
        fator = N * (i)
    else:
        fator = (fator * i)
print(fator)
