def cfor(first, test, update):
    while test(first):
        yield first
        first = update(first)


def exch(a: list, x, y):
    a[x], a[y] = a[y], a[x]


def print_split():
    print('-------------------------------------------------------------------------------------------')
