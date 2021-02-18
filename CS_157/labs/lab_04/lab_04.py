# Richard Hayes Crowley
# CSC_157_LAB_04

print("Richard Hayes Crowley\nCSC_157_LAB_04\n")
print("~*~*~*~ Interest Calculator ~*~*~*~\n")
bankBalance = 0.0
interestRate = 0.0
auth = False

# In a real world application, the pin number would be stored as a hashed value in a secure database on a secure server with strict origin access control, accessible via API.
pinNumber = 1234
attempts = 3

# using a while loop to catch exceptions and continue asking for user input if user mistakenly enters something the interpeter cannot parse as Int
while True:
    try:
        userInput = int(input("Please enter your four-digit PIN: "))
    except ValueError:
        print("Please enter a four digit number.")
        continue
    if userInput == pinNumber:
        auth = True
        break
    elif attempts > 1:
        attempts -= 1
        print("Wrong PIN, please try again.")
    else:
        attempts -= 1
        break


if(auth):
    while True:
        try:
            bankBalance = float(input("Enter an initial bank balance: "))
            interestRate = float(
                input("Enter annual interest rate (as a decimal): "))
            break
        except ValueError:
            print(
                "Please enter a number for initial bank balance and annual interest rate.")

    for month in range(12):
        interest = bankBalance * (interestRate / 12)
        bankBalance += interest
        print(f"Month {month+1} end balance: ${round(bankBalance,2)}")
    print("Goodbye!")
else:
    print("Too many authentication attempts, please try again later.")
