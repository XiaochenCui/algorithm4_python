def queens_lex(n):
    a = list(range(n))
    up = [True]*(2*n - 1)
    down = [True]*(2*n - 1)
    def sub(i):
        if i == n:
            yield tuple(a)
        else:
            for k in range(i, n):
                a[i], a[k] = a[k], a[i]
                j = a[i]
                p = i + j
                q = i - j + n - 1
                if up[p] and down[q]:
                    up[p] = down[q] = False
                    yield from sub(i + 1)
                    up[p] = down[q] = True
            x = a[i]
            for k in range(i + 1, n):
                a[k - 1] = a[k]
            a[n - 1] = x
    yield from sub(0)

for i in queens_lex(8):
    print(i)