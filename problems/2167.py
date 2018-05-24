n = int(input())
rpm = input().split()
a = 0
for i in range(n):
    rpm[i] = int(rpm[i])
for i in range(1, n):
    if rpm[i] < rpm[i-1]:
        a = i+1
        break
print(a)
