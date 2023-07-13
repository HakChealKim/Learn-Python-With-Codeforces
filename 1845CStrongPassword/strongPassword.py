def match(s1, s2, s: str) -> bool:
    idx = -1
    for i in range(len(s1)):
        start = idx + 1
        for x in range(ord(s1[i]), ord(s2[i]) + 1):
            target = chr(x)
            no_match = True
            for v in range(start, len(s)):
                if target == s[v]:
                    idx = max(idx, v)
                    no_match = False
                    break
            if no_match:
                return True
    return False


t = int(input())
for _ in range(t):
    s, m, l, r = input(), int(input()), input(), input()
    flag = match(l, r, s)
    if flag:
        print("YES")
    else:
        print("NO")
