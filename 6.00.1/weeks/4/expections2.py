while True:
    try:
        n = int(input("please enter an integer"))
        break
    except ValueError:
        print("input is not an integer, try again!")
print("Hurray! an integer")
