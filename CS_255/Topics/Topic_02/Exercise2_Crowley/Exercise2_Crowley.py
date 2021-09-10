# Richard Hayes Crowley
# CSC_255_Exercise_02
from os import listdir

from quickSort import quickSort
from bucketSort import bucketSort


def main():
    inputList = []

    for file in listdir("."):
        # find all files in current directory that end in .txt

        if file.startswith("in") and file.endswith(".txt"):

            # break into list of lines
            lines = [line for line in open(file, 'r')]
            # pop out first line item, which is our constant k
            k = lines.pop(0)
            # join list of lines into string and then split on blank \n spaces
            joinedList = "".join(lines).split()
            # flatten list of lines, typecasting strings into integers
            flat_list = [int(string) for string in joinedList]
            # # append k and remaining lines as a tuple
            inputList.append((int(k), flat_list))

    # for each result in result list, write output file
    for input in inputList:
        #  run bucket sort, output A
        with open(f"out{len(input[1])}a.txt", 'w') as f:
            sortedInput = bucketSort(input[1], input[0])
            f.writelines(f'{s}\n' for s in sortedInput)
            # print to command line
            print(
                f"Bucket sort result for input with {len(input[1])} integers: {[s for s in sortedInput]}\n")
        # run quick sort, output B
        with open(f"out{len(input[1])}b.txt", 'w') as f:

            sortedInput = quickSort(input[1])

            f.writelines(f'{s}\n' for s in sortedInput[0])
            # print to command line
            print(
                f"Quick sort result for input with {len(input[1])} integers: {[s for s in sortedInput]}\n")


if __name__ == "__main__":
    main()
