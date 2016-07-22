from datetime import date


def _cmp(x, y):
    return 0 if x == y else 1 if x > y else -1


class Date(date):
    def __new__(cls, string: str = None):
        str_list = string.split('/')
        year = int(str_list[2])
        month = int(str_list[0])
        day = int(str_list[1])
        self = date.__new__(cls, year, month, day)
        return self

    def __repr__(self):
        return '{type}: {year}-{month}-{day}'.format(type=self.__class__.__name__,
                                                     year=self.year,
                                                     month=self.month,
                                                     day=self.day)

    __str__ = __repr__


class Transaction():
    def __new__(cls, string: str = None):
        str_list = string.split()
        self = object.__new__(cls)
        self.who = str_list[0]
        self.data = Date(str_list[1])
        self.amount = float(str_list[2])
        return self

    def __repr__(self):
        return '{type}: {who} {data} {amount}'.format(type=self.__class__.__name__,
                                                      who=self.who,
                                                      data=self.data,
                                                      amount=self.amount)

    __str__ = __repr__

    # Comparisons of Transaction objects with other.

    def __eq__(self, other):
        if isinstance(other, Transaction):
            return self._cmp(other) == 0
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Transaction):
            return self._cmp(other) != 0
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Transaction):
            return self._cmp(other) <= 0
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Transaction):
            return self._cmp(other) < 0
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Transaction):
            return self._cmp(other) >= 0
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Transaction):
            return self._cmp(other) > 0
        return NotImplemented

    def _cmp(self, other):
        assert isinstance(other, Transaction)
        return _cmp(self.amount, other.amount)


if __name__ == '__main__':
    a = Date(string='5/22/1999')
    print(a)
    print(a.__repr__())
    print('--------------------------------------------------------')
    b = Transaction('Turing 8/31/2001 19.00')
    print(b)
    print(b.__repr__())
    print('--------------------------------------------------------')
    c = Transaction('Turing 8/31/2011 19.00')
    print(b == c)
