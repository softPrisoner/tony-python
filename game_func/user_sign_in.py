class signUp:
    sign = 0

    def sign_in_check(self, number):

        sign_result = []
        for n in range(0, 32):
            cond = number & (1 << n)
        if cond > 0:
            sign_result.append(n + 1)
        return sign_result

    # id value
    def sign_in(self, day):
        return self.sign += (1 << day)

# 11
# 1  001
# 2  010
# 3 011
# 4 100


if __name__ == '__main__':
    sign_result = sign_in(8)
    for item in sign_result:
        print(item)
