from sort.merge import merge
from tool import exch


def sort(a: list, lo=None, hi=None):
    if lo is None:
        sort(a, 0, len(a) - 1)
        return
    if hi <= lo:
        return
    j = partition(a, lo, hi)
    sort(a, lo, j - 1)
    sort(a, j + 1, hi)


def partition(a, lo, hi):
    i, j = lo+1, hi
    mid = a[lo]
    while True:
        while a[i] < mid:
            if i == hi:
                break
            i += 1
        while a[j] > mid:
            if j == lo:
                break
            j -= 1
        if i >= j:
            break
        exch(a, i, j)
    exch(a, lo, j)
    return j


if __name__ == '__main__':
    a = [1, 9, 3, 0, 0, 3, 2, 88, 35]
    sort(a)
    print(a)
