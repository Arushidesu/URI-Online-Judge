N = int(input())
T1 = input()
T = T1.split()
for i in range(len(T)):
    T[i] = int(T[i])
menor = min(T)
for i in range(N):
    if menor == T[i]:
        cont = i+1
        break
print(cont)
