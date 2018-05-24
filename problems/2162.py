n = int(input())
h = input().split()
cond = True
for i in range(n):
    h[i] = int(h[i])
if h[1] > h[0]:
    for i in range(1, n-1):
        if i % 2 == 0:
            if h[i+1] <= h[i]:
                cond = False
        else:
            if h[i+1] >= h[i]:
                cond = False
elif h[1] < h[0]:
    for i in range(1, n-1):
        if i % 2 == 0:
            if h[i+1] >= h[i]:
                cond = False
        else:
            if h[i+1] <= h[i]:
                cond = False
else:
    cond = False
print(1 if cond else 0)
