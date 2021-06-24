from counter import Counter


def fib(n, counter):
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n-1, counter) + fib(n-2, counter)


problemSize = 2

# print(f"{'Problem Size':12s}{'Counter':15s}")

for count in range(5):
    counter = Counter()
    # start
    fib(problemSize, counter)
    # end
    # print(f"{problemSize:12d}{counter:15s}")
    problemSize *= 2
