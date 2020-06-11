import calendar
import time
# fetch the calendar


def calendar_test():
    cal = calendar.month(2016, 1)
    print(cal)
# is leap year or plain  year


def isleap(year):
    year = 2019 if not isinstance(year, int) else year
    print(calendar.isleap(year))


def cmpLeapNumBetween(year1, year2):
    if year1 > year2:
        year1, year2 = year2, year1
    return calendar.leapdays(year1, year2)


if __name__ == "__main__":
    calendar_test()
    isleap(2012)
    print(cmpLeapNumBetween(2012, 2019))
