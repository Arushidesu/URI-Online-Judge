hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
V = int(input())
result = []
while V > 0:
    result.append(hex[V % 16])
    V = V // 16
for i in range(len(result) -1, -1, -1):
    print(result[i], end='')
print()
