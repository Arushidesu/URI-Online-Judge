for i in range(int(input())):
    tec = input()
    r, g, b = map(int, input().split())
    if tec == "eye":
        print("Caso #{}: {}" .format(i+1, int((0.3 * r) + (0.59 * g) + (0.11 * b))))
    elif tec == "mean":
        print("Caso #{}: {}" .format(i+1, int((r + g + b) / 3)))
    elif tec == "max":
        print("Caso #{}: {}" .format(i+1, int(max([r, g, b]))))
    else:
        print("Caso #{}: {}" .format(i+1, int(min([r, g, b]))))
