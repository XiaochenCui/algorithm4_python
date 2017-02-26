from copy import deepcopy

from cxctools.print import print_split


def counting(a: list, R):
    """

    Args:
        a:
        R:

    Returns:

    """
    N = len(a)
    count = [0 for i in range(R + 2)]

    # 1.Compute frequency counts.
    for i in range(N):
        count[a[i][1] + 1] += 1

    # 2.Transform counts to indices.
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # 3.Distribute the date.
    aux = [None for i in range(N)]
    for i in range(N):
        aux[count[a[i][1]]] = a[i]
        count[a[i][1]] += 1

    # 4.Copy back.
    a = deepcopy(aux)

    return a


if __name__ == '__main__':
    a = [('Anderson', 2),
         ('Brown', 3),
         ('Davis', 3),
         ('Garcia', 4),
         ('Harris', 1),
         ('Jackson', 3),
         ('Johnson', 4),
         ('Jones', 3),
         ('Martin', 1),
         ('Martinez', 2), ]
    b = counting(a, 4)
    for i in b:
        print(i)
