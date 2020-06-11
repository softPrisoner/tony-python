class classTest:
    i = 12345
    # init method invoke in creating  class object

    def __init__(self):
        print('init method')

    def f(self):
        return 'Hello Wolrd'


class BaseClass:
    # basic property
    name = None
    age = None
    __address = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
# class method must  convert the param  'self' as the first param

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def __private_method(self):
        print('self method')

    def _del_(self):
        print("this destroy method")


class ExtendClass(BaseClass):
    pass


if __name__ == "__main__":
    # x=classTest()
    # print(x.f())
    test2 = BaseClass("tony", 22)
    # classTest2.name
    # classTest2.age
    # AttributeError: type object 'BaseClass' has no attribute '__address'
    # print(BaseClass.__address)
    age = test2.getAge()
    name = test2.getName()
    print("the name is "+name+" age is "+str(age))
