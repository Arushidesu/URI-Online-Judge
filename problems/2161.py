n = int(input())
r = 6
if n == 0:
    print("{:.10f}" .format(3))
else:
    for i in range(n-1):
        r = 6 + 1 / r
    print("{:.10f}" .format(3 + 1 / r))
