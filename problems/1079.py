N = int(input())
for i in range(N):
    A, B, C = map(float, input().split())
    M = "%.1f" % (((A * 2) + (B * 3) + (C * 5)) / 10)
    print(M)
