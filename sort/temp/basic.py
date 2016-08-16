class Sort(object):
    def __init__(self, array_list: list = None):
        self.array_list = array_list if array_list else [1892, 0, -89, 394, 1, 55, -15, 254, 13, 55, 15, 2345, 22]

    def less(self, i, j):
        return self.array_list[i] < self.array_list[j]

    def greater(self, i, j):
        return self.array_list[i] > self.array_list[j]
    
    @property
    def len(self):
        return len(self.array_list)

    def exch(self, x, y):
        self.array_list[x], self.array_list[y] = self.array_list[y], self.array_list[x]


if __name__ == '__main__':
    pass
