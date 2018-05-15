numlist = [900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romlist = ['CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
N = int(input())
cont = 0
for i in numlist:
	if N >= i:
		div = N // i
		print(div * romlist[cont], end='')
		N = N % i
		if N == 0:
			print()
			break
	cont += 1
