from contextlib  import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"")
    with tag("h1")
    print("This is Title")
    