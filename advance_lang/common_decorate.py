def outer(func):
    def inner(*args, **kwargs):
        print("################")
        return func(*args, **kwargs)
    return inner


@outer
def say(name, age):
    print("my name is %s,I am %d years old " % (name, age))
    return "aaa"


say("tony","21")
