from sort.merge import merge
from tool import cfor


def sort(a: list):
    n = len(a)
    for sz in cfor(1, lambda i: i < n, lambda i: i * 2):
        for lo in cfor(0, lambda i: i < n - sz, lambda i: i + sz * 2):
            merge(a, lo, lo + sz - 1, min(lo + sz + sz - 1, n - 1))


if __name__ == '__main__':
    a = [1, 9, 3, 0, 0, 3, 2, 88,35]
    sort(a)
    print(a)
