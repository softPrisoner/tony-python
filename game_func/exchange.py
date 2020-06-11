def cmp(str1, str2):
    tuple1 = ()
    for i in len(str1):
        if str1[0] == str2[0]:
            i += 1
            continue
        j = i + 1
        while j < len(str1):
            if str1[i] == str2[j]:
                str2[i], str2[j] = str2[j], str2[i]
                tuple1.__add__((str2[i], str2[j]))
            elif str1[i] == str1[j]:
                str2[i], str1[j] = str1[j], str2[i]
                tuple1.__add__((str1[j], str2[i]))
        j += 1
        i += 1
    return tuple1


if __name__ == '__main__':
    cmp(["a", "b", "c"], ["b", "a", "c"])
