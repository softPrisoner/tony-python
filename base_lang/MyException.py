class  MyError(Exception):
    def __init__(self,value):
        self.value=value
    def _str_(self):
        return repr(self.value)

def myexception_test():
    try:
        raise MyError("this  is my error")
    except MyError as e:
        print("My Error has been caughted",e.value)
class Error(Exception):
    """Base class for exceptions in this module."""
    pass
 
class InputError(Error):
    """Exception raised for errors in the input.
 
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
 
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
 
class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.
 
    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """
 
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

def clear_file():
    with open("D://t.txt",'rb') as f:
        for line in f:
            print(line,end=" ")

def py_assert_test():
    try:
        assert 1==2
    except AssertionError as e:
     print("this is  some error")
    else: 
        print('this is assert next code')
    finally:
        print("code is finally")
if __name__ == "__main__":
    #myexception_test()
    #clear_file()
    py_assert_test()
