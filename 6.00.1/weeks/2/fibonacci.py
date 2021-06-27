def fib(x):
    """
    x == the number of month, output == number of females in rabbit pen
    essentially, take the last two months output and add them to get the current x months number of females in rabbit pen 
    Also, note that there are two different invocations of the function, and two
    different base cases...
    because if input 1 and input 2... etc
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


fib(4)
