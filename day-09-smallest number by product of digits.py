while True:

    product = 1
    temp1 = n

    while temp1 > 0:
        digit = temp1 % 10
        product *= digit
        temp1 //= 10

    if product % t == 0:
        return n

    n += 1