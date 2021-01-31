
# Richard Hayes Crowley
# 01/31/2021
# CSC_157_Lab_02
# the restaurant tip calculator

class EmptyValue(Exception):
    """Custom exception for empty restaurant or server name"""
    pass

# some error handling,
# TODO: execute failed input question again after exception, current behavior is the loop restarts at the beginning after an exception


print("Richard Hayes Crowley \n01/31/2021 \nCSC_157_Lab_02")
while True:
    try:
        locale = input("please enter the restaurant location: ")
        if not locale:
            raise EmptyValue

        server = input("please enter the server name: ")

        if not server:
            raise EmptyValue

        subtotal = float(input("please enter the menu check subtotal: "))
        tax = float(input("please enter the total tax amount: "))

    except EmptyValue:
        print("Please enter a restaurant location and server name before continuing")

    except ValueError:
        print("input is not a float type, try again!")

    else:
        break


serviceType = "excellent service"

# process the data

# the first tip level
tip1 = 0.22 * subtotal
tip2 = 0.2 * subtotal
tip3 = 0.18 * subtotal

# the output for the first tip level
# print("for:", serviceType, " ; the tip is $", format(tip1, "0.2f"))
print("\n*** suggested tip: ***\n")

print(
    f"Excellent Service 22% (Tip : ${round(tip1,2):0.2f}; Total: ${round((subtotal + tax + tip1), 2):0.2f})")
print(
    f"Great Service 20% (Tip : ${round(tip2,2):0.2f}; Total: ${round((subtotal + tax + tip2), 2):0.2f})")
print(
    f"Good Service 18% (Tip : ${round(tip3,2):0.2f}; Total: ${round((subtotal + tax + tip3), 2):0.2f})")

print("\n*** we thank you - please visit us again ***\n")
