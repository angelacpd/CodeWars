def dig_pow(n, p):
    n_in = n
    digits = []
    while n > 0:
        digit = n % 10 
        digits.insert(0, digit)
        n = int((n - digit)/10)

        # print(n)
        # print(digits)

    sum_dig_pow = 0
    index = 0
    for power in range(p, p+len(digits)):
        sum_dig_pow += digits[index] ** power
        index += 1
        # print(sum_dig_pow)

    result = 0
    k = 0
    while result < sum_dig_pow:
        k += 1
        result = n_in * k

        if result == sum_dig_pow:
            return k

    return -1


print(dig_pow(89, 1))
print(dig_pow(46288, 3))
print(dig_pow(92, 1))
print(dig_pow(695, 2))
print(dig_pow(1546, 2))
