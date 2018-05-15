x = int(input())
aux = i = 0
while x > 365:
    x -= 365
    aux += 1
print("%d ano(s)" %aux)
aux = 0
while x < 365 and x >= 30:
    x -= 30
    aux += 1
print("%d mes(es)" %aux)
print("%d dia(s)" %x)
