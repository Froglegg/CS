try:
    a = int(input("Give me a number: "))
    b = int(input("Give me another number: "))
    print(f"A/B = {a/b}")
    print(f"A + B = {a + b}")
    print("OK")
except ValueError:
    print("VALUE error, could not convert to number")
except ZeroDivisionError:
    print("could not divide by zero")
except TypeError:
    print("type error")
except:
    print("something else went very wrong")
print("outside")

print("1"/"2")
