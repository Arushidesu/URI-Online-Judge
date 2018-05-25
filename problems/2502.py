while True:
    crip = {}
    crip2 = {}
    try:
        a, b = map(int, input().split())
        p, s = input(), input()
        for i in range(a):
            if s[i].islower():
                crip[s[i].upper()] = p[i]
                crip2[p[i].upper()] = s[i]
            else:
                crip[s[i]] = p[i]
                crip2[p[i]] = s[i]
        for i in range(b):
            frase = input()
            novafrase = ''
            for i in range(len(frase)):
                if frase[i].upper() in crip:
                    if frase[i].isupper():
                        novafrase += crip[frase[i]].upper()
                    elif frase[i].islower():
                        novafrase += crip[frase[i].upper()].lower()
                    else:
                        novafrase += crip[frase[i]].lower()
                elif frase[i].lower() in crip:
                    if frase[i].isupper():
                        novafrase += crip[frase[i]].upper()
                    elif frase[i].islower():
                        novafrase += crip[frase[i].upper()].lower()
                    else:
                        novafrase += crip[frase[i]].lower()
                elif frase[i] in crip:
                    novafrase += crip[frase[i]]
                elif frase[i].upper() in crip2:
                    if frase[i].isupper():
                        novafrase += crip2[frase[i]].upper()
                    elif frase[i].islower():
                        novafrase += crip2[frase[i].upper()].lower()
                    else:
                        novafrase += crip2[frase[i]].lower()
                elif frase[i].lower() in crip2:
                    if frase[i].isupper():
                        novafrase += crip2[frase[i]].upper()
                    elif frase[i].islower():
                        novafrase += crip2[frase[i].upper()].lower()
                    else:
                        novafrase += crip2[frase[i]].lower()
                elif frase[i] in crip2:
                    novafrase += crip2[frase[i]]
                else:
                    novafrase += frase[i]
            print(novafrase)
        print()
    except EOFError:
        break
