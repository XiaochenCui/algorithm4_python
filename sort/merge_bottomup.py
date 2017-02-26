from sort.merge import merge
from cxctools.loop import c_for


def sort(a: list):
    n = len(a)
    for sz in c_for(1, lambda i: i < n, lambda i: i * 2):
        for lo in c_for(0, lambda i: i < n - sz, lambda i: i + sz * 2):
            merge(a, lo, lo + sz - 1, min(lo + sz + sz - 1, n - 1))


if __name__ == '__main__':
    a = [1, 9, 3, 0, 0, 3, 2, 88,35]
    sort(a)
    print(a)
