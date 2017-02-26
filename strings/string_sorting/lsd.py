"""
低位优先的字符串排序
"""
from copy import deepcopy

import numpy as np

from cxctools.print import print_split


def lsd(a: list):
    """
    Sorted a list of strings with same length.

    Args:
        a:
    Returns:
        a:
    """
    n = len(a)
    l = len(a[0])
    R = 255
    aux = [None for i in range(n)]

    for i in range(l - 1, -1, -1):
        count = np.zeros(R + 2, dtype=np.int16)

        # 1.Compute frequency counts.
        for j in a:
            key = ord(j[i])
            count[key + 1] += 1

        # 2.Transform counts to indices.
        for j in range(1, len(count)):
            count[j] += count[j - 1]

        # 3.Distribute the data.
        for j in a:
            key = ord(j[i])
            aux[count[key]] = j
            count[key] += 1

        # 3.Copy data.
        a = deepcopy(aux)

    return a


if __name__ == '__main__':
    a = ['4PGC938',
         '2IYE230',
         '3CI0720',
         '1ICK750',
         '10HV845',
         '4JZY524',
         '1ICK750',
         '3CI0720', ]
    b = lsd(a)
    for i in b:
        print(i)

    print_split()

    c = sorted(a)
    for i in c:
        print(i)
