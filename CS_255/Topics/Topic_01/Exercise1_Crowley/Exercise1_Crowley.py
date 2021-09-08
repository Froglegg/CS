# Richard Hayes Crowley
# CSC_255_Topic_01_Exercise_01

# I hope type hints are OK !
# Using python 3.9
from os import listdir


def sumOfK(k: int, lyst: list[int]) -> tuple:
    ''' 
    sumOfK uses an outer and inner loop to determine whether there exists a pair of integers in a 
    list of integers such that the sum of integer A and integer B are equal to a given integer k

    Inputs: target integer k and list of integers 
    Output: returns a tuple with the target k integer, the integer list, a "yes" or "no" indicating whether a pair of integers exists such that 
    integer A + integer B are equal to the given input k, and a string that displays the two integers and their sum.

    Preconditions: input k must be an integer, and input lyst must be a list of integers    

    Complexity: quadratic O(n^2) 
    '''
    for i in lyst:
        for j in lyst:
            if i + j == k:
                return (str(k), f"{lyst}", "Yes", f"{i} + {j} = {i + j}")
    return (str(k), f"{lyst}", "No", "")


def main():
    resultList = []

    for file in listdir("."):
        # find all files in current directory that end in .txt

        if file.startswith("in") and file.endswith(".txt"):

            # break into list of lines
            lines = [line.strip() for line in open(file, 'r')]

            # execute sumOfK function using second and third lines (target constant and list of integers respectively) and append result to resultsList

            # this step type-casts integers, as well, to satisfy preconditions for sumOfK
            resultList.append(
                sumOfK(int(lines[1]),  [int(i) for i in lines[2].split(" ")]))

    # for each result in result list, write output file
    for idx, result in enumerate(resultList):
        with open(f"out{idx + 1}.txt", 'w') as f:
            f.writelines(f'{s}\n' for s in result)

    # print resultsList to command line
    print(resultList)


if __name__ == "__main__":
    main()
