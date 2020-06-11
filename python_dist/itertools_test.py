import itertools
#itertools is  a tools for your test to split the code
def itertools_test():
    #test to is slice(arr, start ,end0)
    s = itertools.islice(range(30,50),10,20)
    for val  in  s:
        print(val)

if __name__ == "__main__":
    itertools_test() 