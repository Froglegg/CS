import random
import os

from simple_term_menu import TerminalMenu
from array_stack import ArrayStack


def readFile(fileString) -> list:
    # read data from a file, returns list of lines
    try:
        dataCollection = []
        f = open(fileString, "r", encoding="utf-8")
        content = f.read().splitlines()

        # perform file operations
        for line in content:
            dataCollection.append(line)
    except:
        print(f'Could not read {fileString}, are you sure it exists?')
        return False
    finally:
        f.close()
        return dataCollection


def writeFile(fileString, lineList=[]) -> None:
    # write data to a file
    try:
        f = open(fileString + ".csv", "w", encoding="utf-8")
        # perform file operations
        # first line
        for line in lineList:
            f.write(f"{line}\n")
    except:
        print(f'Could not write {fileString}!')
        return False
    finally:
        f.close()
        print(f"{fileString} written with {len(lineList)} lines!")


def generateScript(samples: ArrayStack) -> list:
    scriptList = []

    scriptList.append(f"I started the day by looking for the {samples.pop()}.")
    scriptList.append(f"I planned later to walk to the {samples.pop()}.")
    scriptList.append(f"Surprisingly, I found the {samples.pop()} was empty.")
    scriptList.append(f"I wondered if a {samples.pop()} would appear.")
    scriptList.append(
        f"My aunt must have left my cellular telephone with the {samples.pop()}.")
    scriptList.append(
        f"Yesterday, I forgot to take the {samples.pop()} to the meeting.")

    return scriptList


def main():
    # return list of words from each line
    print("\n~*~*~*~ Writer's Grid ~*~*~*~*~*~")

    wordCollection = readFile("words.csv")

    gridStrings = []
    wordList = []

    for idx, line in enumerate(wordCollection):
        # split line string into array of words
        splitLine = [word for word in line.split(',')]
        # create strings to print grid
        wordString = f"Grid line {idx + 1}: {splitLine}"
        gridStrings.append(wordString)
        # append split words to wordsList to be used as samples in stack
        wordList.append(splitLine)

    # print each line in grid
    for line in gridStrings:
        print(line)

    # flatten word list
    flatWordList = [item for sublist in wordList for item in sublist]

    # instantiate stack
    wordStack = ArrayStack(flatWordList)

    while True:

        choice = TerminalMenu(
            ["Generate Random Script", "View Saved Scripts", "Exit"], title="\nWhat would you like to do?").show()

        if choice == 0:
            # # randomly select a subset of elements ( the stack )
            samples = random.sample([word for word in wordStack], 6)
            randomScript = generateScript(samples)
            print("\nSCRIPT GENERATED\n")

            for line in randomScript:
                print(line)

            save_script = TerminalMenu(
                ["Yes", "No"], title="\nWould you like to save this script?").show()
            if save_script == 0:
                fileName = str(input("Please enter a file name: "))
                writeFile(fileName, randomScript)

        elif choice == 1:
            fileList = []
            # look for all files with csv exentsion in this directory
            for file in os.listdir("./"):
                if file.endswith(".csv") and file != "words.csv" and file != "entropy.csv":
                    fileList.append(file)

            if len(fileList) > 0:
                chooseFile = TerminalMenu(
                    fileList, title="\nWhich script would you like to read?").show()
                openFile = readFile(fileList[chooseFile])
                print(f"\nReading {fileList[chooseFile]}\n")
                for line in openFile:
                    print(line)
            else:
                print("No scripts yet! Please generate a random script and save it.")

        else:
            print("\nGoodbye!\n")
            exit()


if __name__ == "__main__":
    main()
