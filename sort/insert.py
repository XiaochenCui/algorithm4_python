import numpy as np
from cxctools.exchange import exch


def sort(a: list):
    """
    对a进行内部排序，无返回值

    Args:
        a:

    Returns:
        None
    """
    n = len(a)

    # 如果n<=1,直接返回
    if n <= 1:
        return

    for i in range(n):
        for j in range(i, 0, -1):  # 从i到1,step为-1
            if a[j] < a[j - 1]:
                exch(a, j, j - 1)
            else:
                break

    return


def external_sort(a: list, lo=None, hi=None):
    """
    对a[lo]至a[hi]进行外部排序并返回结果,a保持不变

    Args:
        a:
        lo:
        hi:

    Returns:
        aux (list):
    """
    if not lo:
        lo = 0
    if not hi:
        hi = len(a) - 1

    n = hi - lo + 1

    aux = a[lo:hi+1]

    # 如果n<=1,直接返回
    if n <= 1:
        return aux

    for i in range(n):
        for j in range(i, 0, -1):  # 从i到1,step为-1
            if aux[j] < aux[j - 1]:
                exch(aux, j, j - 1)
            else:
                break

    return aux


if __name__ == '__main__':
    a = ['she',
         'sells',
         'seashells',
         'by',
         'the',
         'sea',
         'shore',
         'the',
         'shells',
         'are',
         'surely',
         'seashells', ]

    sort(a)
    for i in a:
        print(i)
