t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    ans = []

    if n % 2 != 0:
        print(-1)
    else:
        cnt = 0
        for x in s:
            if x == '(':
                cnt += 1
            else:
                cnt -= 1

        if cnt != 0:
            print(-1)
        else:
            stk = []
            for i in range(len(s)):
                if not stk or s[i] == '(':
                    stk.append((s[i], i))
                else:
                    if stk[-1][0] == '(':
                        stk.pop()
                    else:
                        stk.append((s[i], i))

            res = ["1"] * n

            if not stk or n == len(stk):
                print("1")
            else:
                while stk:
                    res[stk.pop()[1]] = "2"
                print("2")
            print("".join(res))
