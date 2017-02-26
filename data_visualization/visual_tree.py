import pydot

from Bradley_trees_and_tree_algorithms.binary_tree_node import BinaryTreeNode


class VisualTreeMixin(object):
    """
    使用此 Mixin 的类必须实现以下接口：
        1. self.root
        2. node.children 返回 node 的所有子节点
    """

    def generate_graph(self, file_name='tree.png'):
        self.graph = pydot.Dot(graph_type='graph')

        self.add_tree_edges(self.root)

        self.graph.write_png(file_name)

    def add_tree_edges(self, root: BinaryTreeNode):
        for child in root.children:
            # 计算两个节点的str
            str_a = '{u_key}\n{u_val}\n'.format(u_key=root.key,
                                                u_val=root.value, )
            str_b = '{u_key}\n{u_val}\n'.format(u_key=child.key,
                                                u_val=child.value, )
            if 'size' in vars(root):
                str_a += '(size:{})\n'.format(root.size)
                str_b += '(size:{})\n'.format(child.size)
            if 'balance_factor' in vars(root):
                str_a += '(balance_factor:{})\n'.format(root.balance_factor)
                str_b += '(balance_factor:{})\n'.format(child.balance_factor)
            if 'color' in vars(root):
                str_a += '(color:{})\n'.format(root.color)
                str_b += '(color:{})\n'.format(child.color)

            # 添加连接两个节点的边
            self.add_edge(str_a, str_b)

            # 递归添加子节点
            self.add_tree_edges(child)

    def add_edge(self, str_a, str_b):
        edge = pydot.Edge(str_a, str_b)
        self.graph.add_edge(edge)
