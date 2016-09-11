class Node(object):
    def __init__(self, key=None, init_data=None, next_node=None):
        self.key = key
        self.data = init_data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __repr__(self):
        return '{cls}: {key}--{data}'.format(cls=self.__class__.__name__,
                                             key=self.key,
                                             data=self.data)

    __str__ = __repr__


class TreeNode(object):
    def __init__(self, key=None, init_data=None, head=None, left=None, right=None):
        self.key = key
        self.data = init_data
        self.head = head
        self.left = left
        self.right = right

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def set_head(self):
        pass

    def set_left(self, others):
        assert type(others) == TreeNode
        self.left = others
        others.head = self

    def set_right(self, others):
        assert type(others) == TreeNode
        self.right = others
        others.head = self

    def __repr__(self):
        return '{cls}: (key:{key}, data:{data}, head:{head}, left:{left}, right:{right})' \
            .format(cls=self.__class__.__name__,
                    key=self.key,
                    data=self.data,
                    head=self.head.key if self.head else None,
                    left=self.left.key if self.left else None,
                    right=self.right.key if self.right else None,
                    )

    __str__ = __repr__


if __name__ == '__main__':
    temp = Node('he', 93)
    print(temp.get_data())
    print(temp)
    tn1 = TreeNode('tank', 20)
    tn2 = TreeNode('plane', 99)
    tn3 = TreeNode('ship', 1)
    tn1.left = tn2
    tn1.right = tn3
    tn2.head = tn1
    tn3.head = tn1
    print(tn1)
    print(tn2)
    print(tn3)
