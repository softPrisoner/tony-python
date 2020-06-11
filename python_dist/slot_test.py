class Person:
    __slots__ = ["first_name", "last_name", "phone"]

# init method to descibe the work info1

#default  the python use the dict to save the prop of class
def __init__(self, first_name, last_name, phone):

    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
