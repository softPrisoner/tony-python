'''
pass a function as param  and return another function
'''


def easy_decorate_pattern():
    # this is  my decorate code
   # print("add some beautiful leaf")
    print("make a cate")


def advance_decorate_pattern():
    print("........")
    easy_decorate_pattern()


def final_decorate_pattern(funct):
    def inner():
        print("........")
        funct()
    return inner


f = final_decorate_pattern(easy_decorate_pattern)
f()
