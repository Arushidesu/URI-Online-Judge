l = []
while True:
	try:
		l.append(input())
	except EOFError:
		break
a = []
for i in l:
	if i in a:
		continue
	else:
		a.append(i)
print(len(a))
