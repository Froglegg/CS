# Richard Hayes Crowley
# CSC_255_Lab_02
from os import listdir

from wordSort import wordSort
from quickWordSort import quickWordSort


def main():
    inputList = []

    for file in listdir("."):
        # find all files in current directory that end in .txt

        if file.startswith("in") and file.endswith(".txt"):

            # break into list of lines
            lines = [line for line in open(file, 'r')]

            # pop out first line item, which is our maxValue
            maxValue = lines.pop(0).split("maxValue= ")[1].replace("\n", "")

            # # join list of lines into string and then split on blank \n spaces
            joinedList = "".join(lines).split()

            # # # append maxValue and joinedList as a tuple
            inputList.append((maxValue, joinedList))

    # for each result in result list, write output file
    for input in inputList:

        #  run bucket sort, output A
        with open(f"out_abc{len(input[1])}a.txt", 'w') as f:
            sortedInput = wordSort(lyst=input[1], maxWord=input[0])
            f.writelines(f'{s} ' for s in sortedInput)
            # print to command line
            print(
                f"O(n) wordSort result for input with {len(input[1])} words: {[s for s in sortedInput]}\n")

        # run quick sort, output B
        with open(f"out{len(input[1])}b.txt", 'w') as f:

            sortedInput = quickWordSort(wordList=input[1])[0]
            f.writelines(f'{s} ' for s in sortedInput)
            # print to command line
            print(
                f"Quick Sort result for input with {len(input[1])} words: {[s for s in sortedInput]}\n")


if __name__ == "__main__":
    main()
