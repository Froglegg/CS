# Richard Hayes Crowley
# CSC_255_Lab_03
from os import listdir, remove
from Driver import driver


def main():
    inputList = []

    for file in listdir("."):
        # find all files in current directory that end in .txt
        # if file.startswith("in") and file.endswith(".txt") or file == "7_in_Lab3_Crowley.txt":
        if file == "7_in_Lab3_Crowley.txt":

            # break into list of lines
            lines = [line for line in open(file, 'r')]

            # # join list of lines into string and then split on blank \n spaces
            # convert each item to integer
            joinedList = [int(i) for i in "".join(lines).split()]

            # # # append joined list to input list
            inputList.append((joinedList))

        # remove any output files if they already exist for a fresh start
        if file.startswith("out") and file.endswith(".txt"):
            remove(file)

    randomInputList = []
    sortedInputList = []
    sortedDescInputList = []

    for input in inputList:
        random = input
        sortedInput = sorted(input)
        sortedDescInput = sorted(input, reverse=True)

        randomInputList.append(random)
        sortedInputList.append(sortedInput)
        sortedDescInputList.append(sortedDescInput)

    driver(randomInputList, "Random")
    driver(sortedInputList, "Ascending")
    driver(sortedDescInputList, "Descending")


if __name__ == "__main__":
    main()
