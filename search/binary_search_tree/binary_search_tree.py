from data_structure.node import Node, TreeNode


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def put(self, key, data):
        if self.root:
            self._put(key, data, self.root)
        else:
            self.root = TreeNode(key, data)

    def _put(self, key, data, current_node: TreeNode):
        if current_node.key == key:
            self.data = data
        elif current_node.key > key:
            if current_node.has_left_child():
                self._put(key, data, current_node.left)
            else:
                current_node.left = TreeNode(key, data, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, data, current_node.right)
            else:
                current_node.right = TreeNode(key, data, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result=self._get(key,self.root)
            if result:
                return result.data
            else:
                return None
        else:
            return None

    def _get(self, key, current_node: TreeNode):
        if not current_node:
            return None
        if key == current_node.key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self.get(item):
            return True
        else:
            return False


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.put('a', 4)
    bst.put('s', 9)
    bst.put('n', 1)
    bst.put('z', 15)
    bst.put('a', 2)
    bst.put('b', 3)
    print(bst.root)
    print(bst.root.right)
