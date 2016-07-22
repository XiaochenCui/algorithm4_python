import fileinput
import sys

from basic_data_structures import Stack

from basic_data_structures import Stack
from model import Transaction
from tool import exch, print_split


class PQ(Stack):
    def __init__(self, max_size: int = 0, a: list = None):
        super().__init__()

    def insert(self, item):
        super().push(item)

    def max(self):
        pass

    def min(self):
        pass

    def del_max(self):
        max = 0
        n = len(self.items)
        for i in range(n):
            if self.items[i] > self.items[max]:
                max = i
        exch(self.items, max, n - 1)
        return self.pop()

    def del_min(self):
        min = 0
        n = len(self.items)
        for i in range(n):
            if self.items[i] < self.items[min]:
                min = i
        exch(self.items, min, n - 1)
        return self.pop()

    def is_empty(self):
        return super().is_empty()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    m = 5
    filename = 'tinyBatch.txt'
    pq = PQ(max_size=m + 1)
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
    pq = PQ(max_size=m + 1)
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