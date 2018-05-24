while True:
    try:
        x1, y1, x2, y2, v, r1, r2 = map(int, input().split())
        print("N" if ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5) + (v * 1.5) > r1 + r2 else "Y")
    except EOFError:
        break
