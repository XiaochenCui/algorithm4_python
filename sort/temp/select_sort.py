from tools.print import print_split

from sort.basic import Sort


class SelectSort(Sort):
    def sort(self):
        for i in range(self.len):
            min_index = i
            for j in range(i + 1, self.len):
                if self.less(j, min_index):
                    min_index = j
            self.exch(i, min_index)


if __name__ == '__main__':
    s = SelectSort()
    print(s.__class__.__name__+":")
    print(s.array_list)

    print_split()

    s.sort()
    print(s.array_list)
