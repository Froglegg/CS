x = int(input('enter an integer: '))
if x % 2 == 0:
    if x % 3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("divisible by 2 and not 3")
else:
    print("")
    print("odd")
print("done with conditional")
