"""
高位优先的字符串排序
"""
import numpy as np

from cxctools.string import char_at

from sort import insert

R = 256


class MSD(object):
    def __init__(self, m=15):
        self._M = m

    def sort(self, a):
        self._sort(a, lo=0, hi=len(a) - 1, depth=0)
        return a

    def _sort(self, a, lo, hi, depth):
        """
        以第depth个字符为键将a[lo]至a[hi]排序

        Args:
            a:
            lo:
            hi:
            depth:
        """
        length = hi - lo + 1

        if length <= 1:
            return

        # 如果list长度小于self._M，转为插入排序（对于高位优先的字符串排序，这一步是必需的）
        if length <= self._M:
            a[lo:hi + 1] = insert.external_sort(a, lo, hi)
            return

        # 计算频率
        count = np.zeros(R + 2, dtype=np.int16)
        for i in a[lo:hi + 1]:
            count[char_at(i, depth) + 2] += 1

        # 将频率转换为索引
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # 数据分类
        aux = [None for i in range(length)]
        for i in range(lo, hi + 1):
            index = char_at(a[i], depth) + 1  # 当前字符在count数组中的索引，对于存在的字符，从1开始计数，所以要将返回值+1
            aux[count[index]] = a[i]
            count[index] += 1

        # 回写
        for i in range(length):
            a[lo + i] = aux[i]

        for i in range(R):
            self._sort(a, lo + count[i], lo + count[i + 1] - 1, depth + 1)


if __name__ == '__main__':
    msd = MSD(m=1)

    a = ['she',
         'sells',
         'seashells',
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

    msd.sort(a)
    for i in a:
        print(i)
