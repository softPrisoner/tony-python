# only once
import calendar_test
# include
from time_test import *


def invoke_my_calendar():
    return calendar_test.isleap(2012)


if __name__ == "__main__":
    invoke_my_calendar()
    time_test()
