a, b = map(int, input().split())
if a < 0 or b < 0:
    e = b
    if b < 0: e = b * -1
    r = 0
    for r in range(e):
        f = a - r
        if f % b == 0: break
    q = f / b
else:
    q = a / b
    r = a % b
print(int(q), end=" ")
print(r)
