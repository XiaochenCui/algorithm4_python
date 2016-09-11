class BinaryNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left if True else BinaryNode(1, 1)
        self.right = right if True else BinaryNode(1, 1)
        self.parent = parent if True else BinaryNode(1, 1)
        self.size = 1

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def has_both_child(self):
        return self.has_left_child() and self.has_right_child()

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.has_left_child() or self.has_right_child())

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def set_left(self, others):
        if others:
            others.parent = self
        self.left = others

    def set_right(self, others):
        if others:
            others.parent = self
        self.right = others

    def fresh_size(self):
        size = 1
        if self.has_left_child():
            size += self.left.fresh_size()
        if self.has_right_child():
            size += self.right.fresh_size()
        self.size = size
        return size

    @property
    def min_child(self):
        if self.has_left_child():
            node = self.left
            while node.has_left_child:
                node = node.left
            return node
        else:
            return self

    @property
    def max_child(self):
        if self.has_right_child():
            node = self.right
            while node.has_right_child:
                node = node.right
            return node
        else:
            return self

    def __iter__(self):
        if self.has_left_child():
            for elem in self.left:
                yield elem
        yield self
        if self.has_right_child():
            for elem in self.right:
                yield elem


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def __len__(self):
        if self.root:
            return self.root.size
        else:
            return 0

    def __iter__(self):
        if self.root:
            for elem in self.root:
                yield elem

    def put(self, key, value):
        if self.root:
            self._put(self.root, key, value)
        else:
            self.root = BinaryNode(key, value)

    def _put(self, node: BinaryNode, key, value):
        if key == node.key:
            node.value = value
        elif key < node.key:
            if node.has_left_child():
                self._put(node.left, key, value)
            else:
                node.left = BinaryNode(key, value, parent=node)
        elif key > node.key:
            if node.has_right_child():
                self._put(node.right, key, value)
            else:
                node.right = BinaryNode(key, value, parent=node)
        node.fresh_size()

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            return self._get(self.root, key)
        else:
            raise KeyError

    def _get(self, node: BinaryNode, key):
        if key == node.key:
            return node.value
        elif key < node.key:
            if node.has_left_child():
                return self._get(node.left, key)
            else:
                raise KeyError
        elif key > node.key:
            if node.has_right_child():
                return self._get(node.right, key)
            else:
                raise KeyError

    def __getitem__(self, item):
        return self.get(item)

    def max(self):
        if self.root:
            return self.root.max_child
        else:
            return None

    def min(self):
        if self.root:
            return self.root.min_child
        else:
            return None

    def floor(self, key):
        if self.root:
            return self._floor(self.root, key)
        else:
            return None

    def _floor(self, node: BinaryNode, key):
        if key == node.key:
            return node.left.max_child
        elif key < node.key:
            return self._floor(node.left, key)
        elif key > node.key:
            if key > node.right.min_child:
                return self._floor(node.right, key)
            else:
                return node

    def ceiling(self, key):
        if self.root:
            return self._ceiling(self.root, key)
        else:
            return None

    def _ceiling(self, node: BinaryNode, key):
        if key == node.key:
            return node.right.min_child
        elif key > node.key:
            return self._ceiling(node.right, key)
        elif key < node.key:
            if key < node.left.max_child:
                return self._ceiling(node.left, key)
            else:
                return node

    def select(self, index):
        if self.root:
            return self._select(self.root, index)
        else:
            raise IndexError

    def _select(self, node: BinaryNode, index):
        if index > node.size:
            raise IndexError
        elif index == node.left.size:
            return node
        elif index < node.left.size:
            return self._select(node.left, index)
        elif index > node.left.size:
            return self._select(node.right, index - node.left.size - 1)

    def rank(self, key):
        if self.root:
            return self._rank(self.root, key)
        else:
            raise KeyError

    def _rank(self, node: BinaryNode, key):
        if key == node.key:
            return node.left.size
        elif key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return self._rank(node.right, key) + node.left.size + 1

    def set_root(self, node: BinaryNode):
        if node:
            node.parent = None
        self.root = node

    def delete_min(self):
        if self.root:
            return self._delete_min(self.root)
        else:
            return None

    def _delete_min(self, node: BinaryNode):
        min_node = node.min_child
        if min_node.is_root():
            self.set_root(min_node.right)
        elif min_node.has_right_child():
            min_node.parent.set_left(min_node.right)
        else:
            min_node.parent.set_left(None)
        return min_node

    def delete_max(self):
        if self.root:
            return self._delete_max(self.root)
        else:
            return None

    def _delete_max(self, node: BinaryNode):
        max_node = node.max_child
        if max_node.is_root():
            self.set_root(max_node.left)
        elif max_node.has_left_child():
            max_node.parent.set_right(max_node.left)
        else:
            max_node.parent.set_right(None)
        return max_node

    def delete(self, key):
        if self.root:
            self.root = self._delete(self.root, key)
        else:
            raise KeyError

    def _delete(self, node: BinaryNode, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            node_temp = node
            node = node_temp.right.min_child
            node.right = self._delete_min(node.right)
            node.left = node_temp.left
        node.fresh_size()
        return node

    def __delitem__(self, key):
        self.delete(key)


if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"

    print(mytree[6])
    print(mytree[2])

    for i in mytree:
        print(i.key)
        print(i.value)

    del mytree[3]

    for i in mytree:
        print(i.key)
        print(i.value)
