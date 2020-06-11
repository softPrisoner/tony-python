def str_test():
    var1 = 'Hello World'
    var2 = 'Python Runnoob'
    print(var1[0])
    print(var2[1:5])


def str_test2():
    var1 = 'Hello World'
    print(var1[:5])


def str_test2_exp():
    var1 = "Hello World"


# string connect
def str_connect():
    base_str = 'Hello World'
    print(base_str + "----")


def transfer_str():
    print("\\")
    print("\'")
    print("\"")
    # 响铃？？？？
    print("\a")
    # 退格
    print("\b")
    print("\e")
    print("\000")
    print("\n")
    print("\v")
    print("\t")
    print("\r")
    print("\f")
    print("\o12")
    print("\xOa")
    print("\other")
    repeat_str = 'abc'
    print(repeat_str * 2)
    print("a" in repeat_str)
    print("d" not in repeat_str)
    print("%s, is a %d  year old boy", "tony", 15)
    str.capitalize()


def list_connection():
    a1 = [1, 2, 3]
    a2 = [4, 5, 6]
    a3 = a1 + a2
    print(a3)
    a4 = a1 * 3
    isExist = 1 in a1
    print(a4)
    print(isinstance(a4, int))
    for i in a1:
        print(i)


def list():
    L = ["Google", "Runoob", "Taobao"]
    L1 = L[2]
    L2 = L[-2]
    L3 = L[1:]
