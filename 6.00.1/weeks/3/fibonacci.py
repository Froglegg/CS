num_fib_calls = 0


def fib(n, d):
    global num_fib_calls
    num_fib_calls += 1
    if n in d:
        return d[n]
    else:
        ans = fib(n-1, d) + fib(n-2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 2}
print(fib(30, d))
print(num_fib_calls)
