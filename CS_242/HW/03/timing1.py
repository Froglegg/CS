import time

problemSize = 10000000
print("%12s%16s" % ("Probem Size", "Seconds"))

for count in range(5):
    start = time.time()
    # the start of algorithm
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    # end
    elapsed = time.time() - start
    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2
