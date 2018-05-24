n, m = map(int, input().split())
for i in range(m):
    if input() == "fechou":
        n += 1
    else:
        n -= 1
print(n if n >= 0 else 0)
