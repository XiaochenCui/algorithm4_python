from basic_data_structures import Stack
from model import Transaction
from tool import exch

import fileinput
import sys

from basic_data_structures import Stack
from tool import print_split


class MaxPQ(Stack):
    def __init__(self, max_size: int = 0, a: list = None):
        super().__init__()

    def insert(self, item):
        super().push(item)
        n = len(self.items)
        for i in range(n):
            if self.items[i] > item:
                for j in range(n - 1, i, -1):
                    self.items[j] = self.items[j - 1]
                self.items[i] = item
                break

    def max(self):
        pass

    def min(self):
        pass

    def del_max(self):
        return self.pop()

    def del_min(self):
        pass

    def is_empty(self):
        return super().is_empty()

    def size(self):
        return len(self.items)


class MinPQ(Stack):
    def __init__(self, max_size: int = 0, a: list = None):
        super().__init__()

    def insert(self, item):
        super().push(item)
        n = len(self.items)
        for i in range(n):
            if self.items[i] < item:
                for j in range(n - 1, i, -1):
                    self.items[j] = self.items[j - 1]
                self.items[i] = item
                break

    def max(self):
        pass

    def min(self):
        pass

    def del_max(self):
        pass

    def del_min(self):
        return self.pop()

    def is_empty(self):
        return super().is_empty()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    m = 5
    filename = 'tinyBatch.txt'

    pq = MinPQ(max_size=m + 1)
    for line in fileinput.input(files=filename):
        pq.insert(Transaction(line))
        if pq.size() > m:
            pq.del_min()
    stack = Stack()
    while not pq.is_empty():
        stack.push(pq.del_min())
    for r in stack.items:
        print(r)

    print_split()

    pq = MaxPQ(max_size=m + 1)
    for line in fileinput.input(files=filename):
        pq.insert(Transaction(line))
        if pq.size() > m:
            pq.del_max()
    stack = Stack()
    while not pq.is_empty():
        stack.push(pq.del_max())
    for r in stack.items:
        print(r)

    print_split()
