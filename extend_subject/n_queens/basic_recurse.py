from tools.time import timeit


class Solution(object):
    def __init__(self):
        # board存储一种解法（作为缓存）
        self.board = []
        # boards存储所有解法（作为结果）
        self.boards = []

    @timeit
    def solve_n_queens(self, n):
        """
        :param n: int:
        :return: self.boards: list[list[int]]
        """
        self.board = [0 for i in range(n)]
        self.solve_line(0, n)
        return self.boards

    # 解决前row列
    def solve_line(self, row, n):
        if row == n:
            self.boards.append([i for i in self.board])
            return
        else:
            for col in range(n):
                if self.is_valid(row, col):
                    self.board[row] = col
                    self.solve_line(row + 1, n)
                    self.board[row] = 0

    # 监测(row,col)是否与0~row-1行发生冲突
    def is_valid(self, row, col):
        for i in range(row):
            if self.board[i] == col:
                return False
            if i+self.board[i] == row+col:
                return False
            if i-self.board[i] == row-col:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.solve_n_queens(8)
    for i in r:
        print(i)
    print('These are {n} kinds of permutations.'.format(n=len(r)))
