while True:
    try:
        n = int(input())
        v = input()
        if v.count('1') / n >= 2/3:
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break
