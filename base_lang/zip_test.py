def zip_test():
    books = ['疯狂Kotlin讲义', '疯狂Swift讲义', '疯狂Python讲义']
    prices = [79, 69, 89]
    # 使用zip()函数压缩两个列表，从而实现并行遍历
    for book, price in zip(books, prices):
        print("%s的价格是: %5.2f" % (book, price))


def reversed_test():
    for i in reversed(range(10)):
        print(i)


def sorted_test():
    int_arr = [1, 2, 3, -5, 1, 2]
    print(sorted(int_arr))
    print(sorted(int_arr, reverse=True))


def my_max(x=None, y=None):
    '''
    :param x: 第一个数
    :param y: 第二个数
    :return:  返回值
    比较两个数的大小并返回较大的数值
    '''
    x = 0 if not isinstance(x, (int, float)) else x
    y = 0 if not isinstance(y, (int, float)) else y
    return x if x > y else y


if __name__ == '__main__':
    # zip_test()
    # reversed_test()
    # sorted_test()
    print(my_max())
    print(help(my_max))
