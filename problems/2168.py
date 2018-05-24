m = []
n = int(input())
for i in range(n+1):
    c = input().split()
    for j in range(n+1):
        c[j] = int(c[j])
    m.append(c)
for i in range(n):
    for j in range(1, n+1):
        if sum([m[i][j-1], m[i][j], m[i+1][j-1], m[i+1][j]]) >= 2:
            if j == n:
                print("S")
            else:
                print("S", end="")
        else:
            if j == n:
                print("U")
            else:
                print("U", end="")
