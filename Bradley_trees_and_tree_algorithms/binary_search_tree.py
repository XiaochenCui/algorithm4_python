from Bradley_trees_and_tree_algorithms.binary_tree_node import BinaryTreeNode
from data_visualization.visual_tree import VisualTreeMixin


class BinarySearchTree(VisualTreeMixin):
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

    def __setitem__(self, key, value):
        self.put(key, value)

    def put(self, key, value):
        if self.root:
            self._put(self.root, key, value)
        else:
            self.root = BinaryTreeNode(key, value)

    def _put(self, node: BinaryTreeNode, key, value):
        if key == node.key:
            node.value = value
        elif key < node.key:
            if node.has_left_child():
                self._put(node.left, key, value)
            else:
                node.left = BinaryTreeNode(key, value, parent=node)
        else:
            if node.has_right_child():
                self._put(node.right, key, value)
            else:
                node.right = BinaryTreeNode(key, value, parent=node)

        node.update_size()

    def __getitem__(self, item):
        return self.get(item)

    def get(self, key):
        if self.root:
            return self._get(self.root, key)
        else:
            raise KeyError

    def _get(self, node: BinaryTreeNode, key):
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

    @property
    def max(self):
        if self.root:
            return self.root.max_child
        else:
            return None

    @property
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

    def _floor(self, node: BinaryTreeNode, key):
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

    def _ceiling(self, node: BinaryTreeNode, key):
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

    def _select(self, node: BinaryTreeNode, index):
        if index > node.size:
            raise IndexError
        elif index == node.left.size:
            return node
        elif index < node.left.size:
            return self._select(node.left, index)
        elif index > node.left.size:
            return self._select(node.right, index - node.left.size - 1)

    def nodes(self, lo=None, hi=None):
        if self.root:
            if not lo:
                lo = self.min.key
            if not hi:
                hi = self.max.key
            node_list = []
            self._nodes(self.root, node_list, lo, hi)
            return node_list
        else:
            return None

    def _nodes(self, node: BinaryTreeNode, node_list: list, lo, hi):
        if not node:
            return
        if lo < node.key:
            self._nodes(node.left, node_list, lo, hi)
        if lo <= node.key and node.key <= hi:
            node_list.append(node)
        if hi > node.key:
            self._nodes(node.right, node_list, lo, hi)

    def rank(self, key):
        if self.root:
            return self._rank(self.root, key)
        else:
            raise KeyError

    def _rank(self, node: BinaryTreeNode, key):
        if key == node.key:
            return node.left.size
        elif key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return self._rank(node.right, key) + node.left.size + 1

    def set_root(self, node: BinaryTreeNode):
        if node:
            node.parent = None
        self.root = node

    def delete_min(self):
        if self.root:
            return self._delete_min(self.root)
        else:
            return None

    # return deleted node
    def _delete_min(self, node: BinaryTreeNode):
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

    # return deleted node
    def _delete_max(self, node: BinaryTreeNode):
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

    # return a new subtree root
    def _delete(self, node: BinaryTreeNode, key):
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
            successor = self._delete_min(node.right)
            node.parent.set_child(successor)
            successor.set_left(node.left)
            successor.set_right(node.right)
            node = successor

        node.update_size()
        return node

    def __delitem__(self, key):
        self.delete(key)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree[1] = "z"
    tree[2] = "at"
    tree[3] = "red"
    tree[4] = "blue"
    tree[5] = "fight"
    tree[6] = "yellow"

    print(tree[6])
    print(tree[2])

    tree.generate_graph()

    for i in tree:
        print(i.key)
        print(i.value)

    del tree[3]

    for i in tree:
        print(i.key)
        print(i.value)

    for i in tree.nodes(3, 5):
        print(i.key)
        print(i.value)
