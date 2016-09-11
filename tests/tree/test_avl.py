from nose.tools import eq_

from Bradley_trees_and_tree_algorithms.avl_tree import BinarySearchTree


class TestAvl(object):
    def setup(self):
        self.tree = BinarySearchTree()
        self.tree[1] = "z"
        self.tree[2] = "at"
        self.tree[3] = "red"
        self.tree[4] = "blue"
        self.tree[5] = "fight"
        self.tree[6] = "yellow"

    def teardown(self):
        pass

    def test_size(self):
        eq_(len(self.tree), 6)

    def test_relationship(self):
        for node in self.tree:
            if node.has_left_child():
                eq_(node.left.parent, node)
            if node.has_right_child():
                eq_(node.right.parent, node)
