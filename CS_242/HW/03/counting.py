problemSize = 1000
print("%12s%15s" % ("Problem Size", "Iterations"))
for count in range(5):
    number = 0
    # start
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1
    # end
    print(f"{problemSize:12d}{number:15d}")
    problemSize *= 2
# number of iterations is the square of the problem size

# Problem Size     Iterations
    #     1000        1000000
    #     2000        4000000
    #     4000       16000000
    #     8000       64000000
    #    16000      256000000
