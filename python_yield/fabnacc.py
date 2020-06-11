def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1

# console the readable code with list with more flexiable function invoke.


def fab_yield(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1


def fab_list(max):
    n, a, b = 0, 0, 1

    list = []
    while n < max:
        list.append(b)
        a, b = b, a+b
        n += 1
    return list


#Fab Object
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    #todo this iter non-use
    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a+self.b
            self.n += 1
            return r

        raise StopIteration()


if __name__ == "__main__":
    fab(5)
    print("\t\n #@HYY@Y@@@@@@@@@@@")
    for item in fab_list(5):
        print(item)
