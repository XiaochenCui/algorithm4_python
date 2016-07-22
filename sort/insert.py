from tool import exch


def sort(a: list):
    n = len(a)
    for i in range(n):
        for j in range(i, -1, -1):
            if a[j] < a[j - 1]:
                exch(a, j, j - 1)
            else:
                break
    return a

if __name__ == '__main__':
    a = [1, 9, 3, 0, 0, 3, 2, 88]
    print(sort(a))