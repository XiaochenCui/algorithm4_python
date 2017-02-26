def sort(a: list):
    n = len(a)

    # 如果n<=1,直接返回
    if n <= 1:
        return

    for i in range(n):
            temp = a[i]
            for j in range(i, -1, -1):
                if temp < a[j - 1] and j > 0:
                    a[j] = a[j - 1]
                else:
                    a[j] = temp
                    break

    return


if __name__ == '__main__':
    a = [1, 9, 3, 0, 0, 3, 2, 88]
    print(sort(a))
