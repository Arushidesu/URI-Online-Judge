n = int(input())
total = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == 1001: c = 1.5
    elif a == 1002: c = 2.5
    elif a == 1003: c = 3.5
    elif a == 1004: c = 4.5
    else: c = 5.5
    total = total + (c * b)
print("%.2f" %total)
