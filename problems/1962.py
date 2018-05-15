N = int(input())
for i in range(N):
    T = int(input())
    if T >= 2015:
        T = T - 2015 + 1
        print(T, "A.C.")
    else:
        T = abs(T - 2015)
        print(T, "D.C.")
