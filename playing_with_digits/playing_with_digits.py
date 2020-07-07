# Challenge redone to understand function enumerate


def dig_pow(n, p):
    print(list(enumerate(str(n), start = p)))
    addition = 0
    for key, value in enumerate(str(n), start = p):
        print(key, value)
        addition += pow(int(value), key)
        print(addition)
    print(addition/n)
    return int(addition/n) if addition % n == 0 else -1


print(dig_pow(89, 1))
