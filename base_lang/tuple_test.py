# python tuple can not be modified
def tuple_test():
    tuple1 = ("physics", "chemistry", 1997, 2000)
    tuple2 = (1, 2, 3, 4, 5)
    tuple3 = "a", "b", "c"
    # create empty tuple
    tuple4 = ()
    # includes one element need ,
    tuple5 = ("first ele",)
    print("tuple[2]:"+str(tuple1[2]))
    print("tuple[1:2]"+str(tuple1[1:2]))
    print("connect tuple:"+str(tuple1+tuple2))
    # before delete
    print(str(tuple1))
    # delete tuple
    del tuple1
    # after delete  it will emit
   # UnboundLocalError: local variable 'tuple1' referenced before assignment
    print(str(tuple1))


if __name__ == "__main__":
    tuple_test()
