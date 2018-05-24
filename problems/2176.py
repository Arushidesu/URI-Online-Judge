bit = input()
soma = 0
for i in bit:
    soma += int(i)
print(bit + '0' if soma % 2 == 0 else bit + '1')
