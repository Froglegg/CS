# expect 310
balance = 3329
annualInterestRate = 0.2


interest_rate = (annualInterestRate) / 12.0
init_balance = balance
min_fixed_payment = init_balance / 12

interest = 0
for i in range(12):
    updated_balance = balance - min_fixed_payment
    interest += (interest_rate * updated_balance)

    balance = updated_balance + interest

    min_fixed_payment = (init_balance + interest) / 12

print("Lowest Payment: " + str(int(round(min_fixed_payment, -1))))
