# in python string tuples numbers is not been modified
def keywordfunc(name, age):
    print("%s is a %d year old boy", name, age)


def keywordfunc2(name, age=13):
    print(name+"   "+str(age))


def unboundparam(arg1, *vartuple):
    print("输出:")
    print(arg1)
    for item in vartuple:
        print(item)


if __name__ == "__main__":
    keywordfunc(age=15, name="peter")
    keywordfunc2('peter2')
    tuple_T = (1, 2, 3, 4, 5)
    unboundparam("unbound", tuple_T)
    # lambda function anonymous
    def sum(num1, num2): return num1+num2
    print(sum(1, 2))
