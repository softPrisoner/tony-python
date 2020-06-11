import time
# test time moudle


def time_test():
    ticks = time.time()
    print("current time stamp is "+str(ticks))
    localtime = time.localtime(time.time())
    print("current time is "+str(localtime))
    format_localtime = time.asctime(localtime)
    print("format time is "+format_localtime)
    # time.strftime(format[, t])
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == "__main__":
    time_test()
