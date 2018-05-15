h, n = map(int, input().split())
c = input().split()
cont = 0
for i in range(len(c)):
	c[i] = int(c[i])
pode = True
for i in range(len(c)-1):
  if not abs(c[i] - c[i+1]) <= h:
	  pode = False
	  break
if pode:
	print("YOU WIN")
else:
	print("GAME OVER")
