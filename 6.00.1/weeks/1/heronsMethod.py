# Heron's method, ancient algorithm for finding square roots of y * y = x
# start with a guess, let's say, 3 is the square root of sixteen (3*3 = 16) obv wrong
# if guess * guess is close enough, stop and supply the answer
# otherwise, make a new guess by averaging g and x / g
# repeat process until close enough
import numpy as np
import fire


def herons_method(guess, number, iterations=1):

    if(number < 0):
        return print(f"{number} is a negative number... negative numbers cannot have square roots.")
    if(guess < 0 or guess > number):
        return print(f"Either {guess} is a negative number, or its value is greater than {number}... please supply a positive number greater than {number} as a guess.")
    if(guess**2 == number):
        return print(f"Heron's method returns {guess} as a close enough square root for {number} after {iterations} iterations.")

    iterations = iterations + 1
    new_guess = np.average([guess, (number/guess)])
    herons_method(new_guess, number, iterations)


if __name__ == '__main__':
    fire.Fire(herons_method)

# herons_method(123, 321)
# use the command line, run `python herons_method 123 321`
