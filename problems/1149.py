A = N = cont = 0
AN = input().split(" ")
for i in range(len(AN)):
    if int(AN[i]) > 0 and A == 0:
        A = int(AN[i])
    elif int(AN[i]) > 0:
        N = int(AN[i])
        break
for i in range(N):
    cont = A + i + cont
print(cont)
