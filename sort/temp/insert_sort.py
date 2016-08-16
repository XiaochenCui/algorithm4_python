from tools.print import print_split

from sort.basic import Sort


class InsertSort(Sort):
    def sort(self):
        for i in range(self.len):
            for j in range(i, 0, -1):
                if self.less(j, j - 1):
                    self.exch(j, j - 1)


if __name__ == '__main__':
    s = InsertSort()
    print(s.__class__.__name__ + ":")
    print(s.array_list)

    print_split()

    s.sort()
    print(s.array_list)
