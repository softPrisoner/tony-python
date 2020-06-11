import functools

print(int("1010",base=2))

f =functools.partial(int,base=2)
print(f("1011"))