N = int(input())
for i in range(N):
    X, Y = map(float, input().split())
    if Y == 0:
        print("divisao impossivel")
    else:
        R = "%.1f" % (X / Y)
        print(R)
