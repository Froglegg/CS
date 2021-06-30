coins = [50, 25, 10, 5, 1]
amount = 0
count = 0
i = 0
print("please enter the amount you wish to change : ")
amount = int(input())
print("----------------------------")
for i in range(len(coins)):
    count = int(amount / coins[i])
    if (count != 0):
        print("count of {0} cent(s) : {1}" . format(coins[i], count))
        amount %= coins[i]
