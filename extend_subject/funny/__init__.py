import random


class A(object):
    def __init__(self):
        self.level = random.choice(B.LEVEL)


class B(object):
    LEVEL = [1,2,3]


if __name__ == '__main__':
    a = A()
    print(a.level)