def dictionary_test():
    dict = {'a': 1, 'b': 2, 'b': 3}
    print(dict['b'])
    # {'a': 1, 'b': 3} from the  result can know about
    # if repeat key exsits last elements will replace others
    print(dict)


def dictionary_test2():
    dict1 = {'abc': 456}
    dict2 = {'abc': 123, 98.6: 37}
    print(dict1)
    print(dict2)


def dictionary_test3():
    dict = {"k1": "v1", "k2": "v2"}
    # before update
    print("before update:"+str(dict))
    # update the k1
    dict["k1"] = "v11"
    print("after update:"+str(dict))
    # if not exist add
    dict["k3"] = "v3"
    # afer add val
    print("add k3:v3"+str(dict))
    # delete dict element
    del dict["k1"]

    # dict.clear()


if __name__ == "__main__":
    dictionary_test2()
# dict type fakes as map with the key and value.
