import pydot

from Bradley_trees_and_tree_algorithms.binary_tree_node import BinaryTreeNode


class VisualTreeMixin(object):
    def generate_graph(self, file_name='tree.png'):
        self.graph = pydot.Dot(graph_type='graph')

        self.add_tree_edges(self.root)

        self.graph.write_png(file_name)

    def add_tree_edges(self, root: BinaryTreeNode):
        for child in root.children:
            self.add_edge('{u_key}\n{u_val}\n(size:{size})\n(balance_factor:{balance_factor}\n(color:{color})'
                          .format(u_key=root.key,
                                  u_val=root.value,
                                  size=root.size,
                                  balance_factor=root.balance_factor,
                                  color=root.color),
                          '{d_key}\n{d_val}\n(size:{size})\n(balance_factor:{balance_factor}\n(color:{color})'
                          .format(d_key=child.key,
                                  d_val=child.value,
                                  size=child.size,
                                  balance_factor=child.balance_factor,
                                  color=child.color),
                          )
            self.add_tree_edges(child)

    def add_edge(self, str_a, str_b):
        edge = pydot.Edge(str_a, str_b)
        self.graph.add_edge(edge)
