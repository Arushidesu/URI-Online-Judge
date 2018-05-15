x, y = map(int, input().split())
aux = 0
if y > x:
    r = y - x
    print("O JOGO DUROU %d HORA(S)" %r)
elif x == y:
    print("O JOGO DUROU 24 HORA(S)")
elif x > y:
    r = 24 - x + y
    print("O JOGO DUROU %d HORA(S)" %r)
