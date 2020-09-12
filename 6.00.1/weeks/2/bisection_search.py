x = 25
epsilon = 0.01
guesses = 0
low = 0.0
high = x
ans = high + low / 2

while abs(ans**2 - x) >= epsilon:
    print(f"Low: {low} High: {high} ANS:{ans}")
    guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print(f"num of guesses: {guesses}")
print(f"{str(ans)} is close to the sq root of {x}")

# cubed root

x = 27
epsilon = 0.01
guesses = 0
low = 0.0
high = x
ans = high + low / 2

while abs(ans**3 - x) >= epsilon:
    print(f"Low: {low} High: {high} ANS:{ans}")
    guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print(f"num of guesses: {guesses}")
print(f"{str(ans)} is close to the cubed root of {x}")
