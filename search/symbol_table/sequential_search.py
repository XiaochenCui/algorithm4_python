from tools.data_structure.node import Node
from tools.time import timeit

from data_visualization.visual_accumulator import VisualAccumulator


class SequentialSearchST(object):
    def __init__(self):
        self.first = Node()
        self.max = Node(init_data=0)

    def get(self, key):
        # 根据指定的key返回data，没找到key则返回None
        node = self.first
        while node:
            if key == node.key:
                return node.data
            node = node.next
        return None

    def put(self, key, data):
        # 将指定的key的data值置为data，没找到key则插入为头节点
        node = self.first
        cmp_times = 0
        while node:
            cmp_times += 1
            if key == node.key:
                node.data = data
                # update self.max
                if data > self.max.data:
                    self.max = node
                return cmp_times
            node = node.next
        self.first = Node(key, data, self.first)
        return cmp_times

    def __contains__(self, key):
        node = self.first
        while node:
            if key == node.key:
                return True
            node = node.next
        return False

    @property
    def keys(self):
        # 以列表形式返回所有key
        key_list = []
        node = self.first
        while node:
            if node.key:
                key_list.append(node.key)
            node = node.next
        return key_list


@timeit
def main(file, n=0):
    va = VisualAccumulator(20, 20)

    st = SequentialSearchST()

    with open(file, 'r') as f:
        for line in f:
            for word in line.split():
                if len(word) < n:
                    continue
                elif word not in st:
                    cmp_times = st.put(word, 1)
                    va.add_data_value(cmp_times)
                else:
                    cmp_times = st.put(word, st.get(word) + 1)
                    va.add_data_value(cmp_times)

    print(st.max)


if __name__ == '__main__':
    min_len = 0

    # 查找双城记的前2000行，过滤长度小于8的单词
    main(file='../file/tinyTale.txt', n=min_len)
