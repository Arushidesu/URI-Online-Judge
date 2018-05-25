n = int(input())
k = int(input())
p = []
c = []
for i in range(n):
    p.append(int(input()))
while True:
    if len(c) >= k and min(c) not in p:
        break
    else:
        c.append(max(p))
        p.remove(max(p))
print(len(c))
