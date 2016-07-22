import fileinput
import sys

from basic_data_structures import Stack
from model import Transaction
# from sort.priority_queue.pq_array_disorder import PQ
from sort.priority_queue.pq_array_order import MaxPQ, MinPQ

if __name__ == '__main__':
    m = int(sys.argv[1])
    filename = sys.argv[2]
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
