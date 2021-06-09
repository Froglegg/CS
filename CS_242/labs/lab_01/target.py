import decimal

# Had some trouble with Python's native "round" and formatting functions when dealing with rounding up floating points such as 3.025, had to do some googling to find a solution
# round_up def is taken from https://stackoverflow.com/questions/9232256/round-up-to-second-decimal-place-in-python


def round_up(x, place=0):
    context = decimal.getcontext()
    # get the original setting so we can put it back when we're done
    original_rounding = context.rounding
    # change context to act like ceil()
    context.rounding = decimal.ROUND_CEILING

    rounded = round(decimal.Decimal(str(x)), place)
    context.rounding = original_rounding
    return float(rounded)


print("Program: Target GPA")
print("Programmer: Richard Hayes Crowley")
print("-------------------------")

print(round(3.025, 2))

# ---------------------------------------------------
# variables declared and initialized
msg1 = ""
msg2 = ""
msg3 = ""
msg4 = ""
totalHours = 0
creditsEarned = 0
creditsCurrent = 0
currentGPA = 0
targetGPA = 0
targetGradePoints = 0
requiredGPA = 0
bestPossibleGPA = 0
# ... declare and assign any additional variables here ...

# ---------------------------------------------------
print("----- INPUTING Data -----")

msg1 = "GPA credit hours already completed ( Credits Earned ) "
creditsEarned = int(input("Enter " + msg1))
msg2 = "current GPA ( Cumulative ) "
currentGPA = float(input("Enter " + msg2))
msg3 = "credit hours currently enrolled ( Remaining / Planned Credits )"
creditsCurrent = int(input("Enter " + msg3))
msg4 = "the desired Target GPA"
targetGPA = float(input("Enter " + msg4))

# ---------------------------------------------------
print("----- PROCESSING Data -----")

totalHours = creditsEarned + creditsCurrent
targetGradePoints = targetGPA * totalHours
targetGradePoints -= creditsEarned * currentGPA
requiredGPA = targetGradePoints / creditsCurrent

bestPossibleGPA = ((creditsEarned * currentGPA +
                    creditsCurrent * 4) / (creditsEarned + creditsCurrent))

# ---------------------------------------------------
print("----- OUTPUTTING Data -----")

# ... complete the output section of this program ...
print("\n**** GPA REPORT ****\n")
print(f"Current GPA: {currentGPA:0.2f}")
print(f"Credits Earned: {creditsEarned}")
print(f"Target (desired) GPA: {targetGPA:0.2f}")
print(f"Remaining Credits: {creditsCurrent}\n")

print(
    f"To attain the desired GPA of {targetGPA} , you will require {creditsCurrent} credit hours with a GPA of {round_up(requiredGPA,2):0.2f}")

print(
    f"Your best possible GPA will be {round_up(bestPossibleGPA,2):0.2f} ( assuming all A's for your remaining credits )")
