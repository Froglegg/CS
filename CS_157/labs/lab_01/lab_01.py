# Richard Hayes Crowley
# 01/28/2021
# CS_157_Lab_01

print("\nRichard Hayes Crowley\n01/28/2021\nCS_157_Lab_01\n")

totalCost = 0.0
appName = ""
costPerKW = 0.0
annualUsage = 0.0


class EmptyValue(Exception):
    """Custom exception for empty appliance name"""
    pass


print("[ please enter the requested data ]")

for i in range(6):
    while True:
        try:
            appName = input("appliance name: ")
            if not appName:
                raise EmptyValue
            costPerKW = float(
                input("cost per KW - hr of the appliance (in cents): "))
            annualUsage = float(input("annual usage (in KW - hr): "))
            break
        except EmptyValue:
            print("Please enter an appliance name before continuing")
        except ValueError:
            print("input is not a float type, try again!")
    totalCost += annualUsage*costPerKW
    print("")

print(f"The total cost of the annual usage is: ${round(totalCost,2)}")
