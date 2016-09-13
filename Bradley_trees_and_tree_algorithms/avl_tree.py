from Bradley_trees_and_tree_algorithms.binary_search_tree import BinarySearchTree
from Bradley_trees_and_tree_algorithms.binary_tree_node import BinaryTreeNode
from data_visualization.visual_tree import VisualTreeMixin


class AVLTree(BinarySearchTree):
    def _put(self, node: BinaryTreeNode, key, value):
        if key == node.key:
            node.value = value
        elif key < node.key:
            if node.has_left_child():
                self._put(node.left, key, value)
            else:
                node.left = BinaryTreeNode(key, value, parent=node)
                self.update_balance(node.left)
        elif key > node.key:
            if node.has_right_child():
                self._put(node.right, key, value)
            else:
                node.right = BinaryTreeNode(key, value, parent=node)
                self.update_balance(node.right)
        node.update_size()

    def update_balance(self, node: BinaryTreeNode):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.has_parent():
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    # 平衡节点node并事先检查继任节点的平衡性
    # （默认前提：继任节点的balance_factor在-1到1之间）
    def rebalance(self, node: BinaryTreeNode):
        # situation 1:right heavy, need rotate_left
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self.rotate_right(node.right)
            self.rotate_left(node)
        # situation 2:left heavy, need rotate_right
        elif node.balance_factor > 1:
            if node.left.balance_factor < 0:
                self.rotate_left(node.left)
            self.rotate_right(node)

    def rotate_left(self, old_root: BinaryTreeNode):
        new_root = old_root.right

        # 1.change upper relationships.
        if old_root.is_root():
            self.set_root(new_root)
        else:
            old_root.parent.set_child(new_root)

        # 2.change old_root's right
        old_root.set_right(new_root.left)
        # 3.change new_root's left
        new_root.set_left(old_root)

        # 4.update two node's size
        old_root.update_size()
        new_root.update_size()

        # 5.change balance factor
        old_root.balance_factor = old_root.balance_factor + 1 - min(0, new_root.balance_factor)
        new_root.balance_factor = new_root.balance_factor + 1 + max(0, old_root.balance_factor)

    def rotate_right(self, old_root: BinaryTreeNode):
        new_root = old_root.left

        # 1.change upper relationships.
        if old_root.is_root():
            self.set_root(new_root)
        else:
            old_root.parent.set_child(new_root)

        # 2.change old_root's left
        old_root.set_left(new_root.right)
        # 3.change new_root's right
        new_root.set_right(old_root)

        # 4.update two node's size
        old_root.update_size()
        new_root.update_size()

        # 5.change balance factor
        old_root.balance_factor = old_root.balance_factor - 1 - max(0, new_root.balance_factor)
        new_root.balance_factor = new_root.balance_factor + 1 + max(0, old_root.balance_factor)


if __name__ == '__main__':
    tree = AVLTree()
    tree[1] = "z"
    tree[2] = "at"
    tree[3] = "red"
    tree[4] = "blue"
    tree[5] = "fight"
    tree[6] = "yellow"
    for i in range(7, 25):
        tree[i] = "test"

    tree.generate_graph()

    for i in range(11, 13):
        del tree[i]
        tree.generate_graph(file_name='tree{}.png'.format(i))
