renas = {1: 'Dasher', 2: 'Dancer', 3: 'Prancer', 4: 'Vixen', 5: 'Comet', 6: 'Cupid', 7: 'Donner', 8: 'Blitzen', 9: 'Rudolph'}
rena = input().split()
for i in range(9):
  rena[i] = int(rena[i])
num = sum(rena) - (9 * (sum(rena) // 9))
print(renas[9] if num == 0 else renas[num]) 
