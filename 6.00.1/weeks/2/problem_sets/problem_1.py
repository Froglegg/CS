# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

#   # Test Case 1:
#   balance = 42
#   annualInterestRate = 0.2
#   monthlyPaymentRate = 0.04

#       # Result Your Code Should Generate Below:
#       Remaining balance: 31.38

#       # To make sure you are doing calculation correctly, this is the
#       # remaining balance you should be getting at each month for this example
#         Month 1 Remaining balance: 40.99
#         Month 2 Remaining balance: 40.01
# ...
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


interest_rate = (annualInterestRate/12.0)

for i in range(12):
    min_payment = monthlyPaymentRate * balance
    unpaid_balance = balance - min_payment
    balance = unpaid_balance + (interest_rate * unpaid_balance)

print("Remaining Balance: " + str(round(balance, 2)))
