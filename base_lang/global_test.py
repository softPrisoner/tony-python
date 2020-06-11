Money = 200
Age = 12


def add_money(plus):
    global Money
    Money = Money+1
    print(Money)
    print(locals())
    print(globals())


def global_test():
    print(Money)


if __name__ == "__main__":
    add_money(12)
    global_test()
