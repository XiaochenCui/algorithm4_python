import fileinput

from basic_data_structures import Stack
from model import Transaction
from tool import exch, print_split


class MinPQ(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percolation_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                exch(self.heap_list, i, i // 2)
            i //= 2

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        self.percolation_up(self.current_size)

    def percolating_down(self, i):
        while i * 2 <= self.current_size:
            min_c = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_c]:
                exch(self.heap_list, i, min_c)
            i = min_c

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            return i * 2 if self.heap_list[i * 2] < self.heap_list[i * 2 + 1] else i * 2 + 1

    def del_min(self):
        val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolating_down(1)
        return val

    def build_heap(self, a_list: list = []):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list
        while i > 0:
            self.percolating_down(i)
            i -= 1

    def is_empty(self):
        return self.heap_list == [0]

    def size(self):
        return self.current_size

    def is_property(self):
        for i in range(1, (self.current_size + 1) // 2):
            if self.heap_list[i] > self.heap_list[self.min_child(i)]:
                return False
        return True


if __name__ == '__main__':
    m = 5
    filename = 'tinyBatch.txt'

    pq = MinPQ()
    for line in fileinput.input(files=filename):
        pq.insert(Transaction(line))
    assert pq.is_property()
    stack = Stack()
    while not pq.is_empty():
        stack.push(pq.del_min())
    for r in stack.items:
        print(r)

    print_split()
