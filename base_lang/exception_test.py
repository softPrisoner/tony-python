def zeroexp():
    try:
        a = 1/0
    except ZeroDivisionError:
        print('there are some erro happened with code block')
    else:
        print("there is no  exception")
    finally:
        print("this is my finally"+a)


def raise_test():
    x = 10
    if x > 5:
        raise Exception("x can't over  5")


if __name__ == "__main__":
    # zeroexp()
    raise_test()
