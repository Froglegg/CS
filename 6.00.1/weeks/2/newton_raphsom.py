y = 245.0
epsilon = 0.001
guess = y / 2.0
numGuesses = 0

while abs(guess * guess - y) >= epsilon:
    numGuesses += 1
    print(numGuesses)
    guess -= ((guess**2 - y) / (2*guess))
print(f"Num. of guesses: {numGuesses}")
print(f"Sq root of {y} is about {guess}")
