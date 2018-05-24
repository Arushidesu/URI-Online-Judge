p, j1, j2, r, a = map(int, input().split())
if r == 1 and a == 1:
    print("Jogador 2 ganha!")
elif (r == 1 and a == 0) or (r == 0 and a == 1):
    print("Jogador 1 ganha!")
else:
    if (((j1+j2) % 2 == 0) and p == 1) or (((j1+j2) % 2 != 0) and p == 0):
        print("Jogador 1 ganha!")
    else:
        print("Jogador 2 ganha!")
