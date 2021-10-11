# Richard Hayes Crowley
# CSC_255_Lab_03
from os import listdir


def main():
    inputList = []

    for file in listdir("."):
        # find all files in current directory that end in .txt

        if file.startswith("in") and file.endswith(".txt"):

            # break into list of lines
            lines = [line for line in open(file, 'r')]

            # # pop out first line item, which is our maxValue
            # maxValue = lines.pop(0).split("maxValue= ")[1].replace("\n", "")

            # # join list of lines into string and then split on blank \n spaces
            joinedList = "".join(lines).split()

            # # # append joined list to input list
            inputList.append((joinedList))

    # for each result in result list, write output file
    for input in inputList:
        with open(f"out_TEST{len(input)}.txt", 'w') as f:

            f.writelines(f'{s} ' for s in input)
            # print to command line


if __name__ == "__main__":
    main()
