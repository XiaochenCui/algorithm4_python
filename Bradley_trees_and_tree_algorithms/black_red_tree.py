from Bradley_trees_and_tree_algorithms import RED, BLACK
from Bradley_trees_and_tree_algorithms.binary_search_tree import BinarySearchTree
from Bradley_trees_and_tree_algorithms.binary_tree_node import BinaryTreeNode


class BlackRedTree(BinarySearchTree):
    def put(self, key, value):
        if self.root:
            self._put(self.root, key, value)
        else:
            self.root = BinaryTreeNode(key, value, color=BLACK)

    def _put(self, node: BinaryTreeNode, key, value):
        # same as bst.
        if key == node.key:
            node.value = value
            return
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

        # rotate and colors change
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and node.left and self.is_red(node.left.left):
            node = self.rotate_right(node)
        self.flip_colors(node)

        node.update_size()

    @staticmethod
    def is_red(node: BinaryTreeNode):
        if node:
            return node.is_red()
        else:
            return False

    def flip_colors(self, node: BinaryTreeNode):
        if self.is_red(node.left) and self.is_red(node.right):
            node.left.color = BLACK
            node.right.color = BLACK
            if not node.is_root():
                node.color = RED

    def rotate_left(self, old_root: BinaryTreeNode):
        new_root = old_root.right

        # 1.change upper relationships.
        if old_root.is_root():
            self.set_root(new_root)
        else:
            old_root.parent.set_child(new_root)

        # 2.change old_root's right
        old_root.set_right(new_root.left)
        # 3.change new root's left
        new_root.set_left(old_root)

        # 4.update color
        new_root.color = old_root.color
        old_root.color = RED

        # 5.update size
        old_root.update_size()
        new_root.update_size()

        return new_root

    def rotate_right(self, old_root: BinaryTreeNode):
        new_root = old_root.left

        # 1.change upper relationships.
        if old_root.is_root():
            self.set_root(new_root)
        else:
            old_root.parent.set_child(new_root)

        # 2.change old_root's left
        old_root.set_left(new_root.right)
        # 3.change new root's right
        new_root.set_right(old_root)

        # 4.update color
        new_root.color = old_root.color
        old_root.color = RED

        # 5.update size
        old_root.update_size()
        new_root.update_size()

        return new_root

    # 尚未完成：
    #   删除操作


if __name__ == '__main__':
    tree = BlackRedTree()
    example = 'searchxmpl'
    for i in example:
        tree[i] = 'test'
    tree.generate_graph()
