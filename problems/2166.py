n = int(input())
r = 2
if n == 0:
    print("{:.10f}" .format(1))
else:
    for i in range(n-1):
        r = 2 + 1 / r
    print("{:.10f}" .format(1 + 1 / r))
