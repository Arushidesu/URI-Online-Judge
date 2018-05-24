s, t, f = map(int, input().split())
r = s + t + f
if r < 0:
    r = 24 + r
elif r > 24:
    r = r - 24
print(r)
