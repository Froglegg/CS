ogNum = -8
num = -8

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    print(result)
    num = num//2
    print(num)
if isNeg:
    result = '-' + result

print(f"binary of {ogNum} is {result}")
