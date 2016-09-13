from Bradley_trees_and_tree_algorithms import RED, BLACK


class BinaryTreeNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None, color=RED):
        self.key = key
        self.value = value
        self.left = left if True else BinaryTreeNode(1, 1)
        self.right = right if True else BinaryTreeNode(1, 1)
        self.parent = parent if True else BinaryTreeNode(1, 1)
        self.size = 1
        self.balance_factor = 0
        self.color = color

    def has_parent(self):
        return self.parent

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

    def set_child(self, others):
        if others:
            if others.key < self.key:
                self.set_left(others)
            else:
                self.set_right(others)

    def update_size(self):
        size = 1
        if self.has_left_child():
            size += self.left.size
        if self.has_right_child():
            size += self.right.size
        self.size = size
        return size

    @property
    def min_child(self):
        if self.has_left_child():
            node = self.left
            while node.has_left_child():
                node = node.left
            return node
        else:
            return self

    @property
    def max_child(self):
        if self.has_right_child():
            node = self.right
            while node.has_right_child():
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

    @property
    def children(self):
        r = []
        if self.has_left_child():
            r.append(self.left)
        if self.has_right_child():
            r.append(self.right)
        return r

    def is_red(self):
        return self.color
