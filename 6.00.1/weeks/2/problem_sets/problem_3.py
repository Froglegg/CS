
#   Test Case 1:
#   balance = 320000
#   annualInterestRate = 0.2

#   Result Your Code Should Generate:
#   -------------------
#   Lowest Payment: 29157.09


# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

balance = 320000
annualInterestRate = 0.2

interest_rate = annualInterestRate/12.0
lower = balance / 12
upper = ((balance * ((1 + interest_rate)**12)) / 12)

epsilon = 0.01
min_payment = (upper + lower) / 2
test_bool = False

while test_bool == False:
    test_balance = balance

    for i in range(12):
        updated_balance = test_balance - min_payment
        test_balance = updated_balance + (interest_rate * updated_balance)
    if round(abs(test_balance), 2) == epsilon:
        test_bool == True
        break
    if test_balance < 0:
        upper = min_payment
    if test_balance > 0:
        lower = min_payment
    min_payment = (upper + lower) / 2

print("Lowest Payment: " + str(round(min_payment, 2)))
