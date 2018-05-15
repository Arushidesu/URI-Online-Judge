while True:
    try:
        aux = 0
        L = int(input())
        v = input()
        v2 = v.split()
        for i in range(len(v2)):
            v2[i] = int(v2[i])
        if max(v2) < 10:
            print("1")
        elif max(v2) < 20:
            print("2")
        else:
            print("3")
    except EOFError:
        break
