def intToStr(i):
    digits = "0123456789"
    if i == 0:
        return "0"
    res = ''
    count = 0
    while i > 0:
        count += 1
        print(i)
        res = digits[i % 10] + res
        print(res)
        i = i//10
    print(f"TOTAL COUNT is {count}")
    return res


intToStr(11111111111111111111)
