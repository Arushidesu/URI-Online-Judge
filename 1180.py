N = int(input())
X = [int(x) for x in input().split()]
for i in range(N):
    if min(X) == X[i]:
        print("Menor valor: %s\n"
              "Posicao: %s" %(X[i], i))
