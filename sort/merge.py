import copy


def sort(a: list, lo=None, hi=None):
    if lo is None:
        sort(a, 0, len(a) - 1)
        return
    if hi <= lo:
        return
    mid = int(lo + (hi - lo) / 2)
    sort(a, lo, mid)
    sort(a, mid + 1, hi)
    merge(a, lo, mid, hi)


def merge(a: list, lo, mid, hi):
    i, j = lo, mid + 1
    aux = copy.deepcopy(a)
    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1


if __name__ == '__main__':
    a = [1, 9, 3, 0, 0, 3, 2, 88]
    sort(a)
    print(a)
