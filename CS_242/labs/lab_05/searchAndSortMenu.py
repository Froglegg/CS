from simple_term_menu import TerminalMenu
from Algorithms import *

listType = ""


def main():
    global listType

    algos = ""
    print("Hello! Welcome to 'Search and Sort', a profiling search and sort tool. Would you like to use your own list or generate an unsorted list?")
    list_choice = TerminalMenu(["Random list", "My own list", "Exit"]).show()

    if list_choice == 0:
        algos = Algorithims()

        list_type = TerminalMenu(["Numeric list", "Word list"],
                                 title="What kind of list would you like to generate?").show()

        listType = "numeric" if list_type == 0 else "word"

        size = input(
            "What size list? Please enter a positive integer: ")
        try:
            size = int(size)
        except ValueError:
            print("That's not an integer! Play nice or leave!")
            return exit()

        if list_type == 0:
            algos.generateNumericList(size)
        else:
            algos.generateWordList(size)

        viewList = input(
            "Would you like to view your unsorted list? Enter 'y' if you would: ")
        if viewList == "y":
            algos.printList()

    elif list_choice == 1:
        listInput = input(
            "Please enter a comma separated list OF THE SAME TYPE OF VALUES (not numbers and words, please): ").split(",")

        algos = Algorithims(listInput)
    else:
        print("goodbye!")
        exit()

    while True:

        sort_or_search = TerminalMenu(
            ["Sort list", "Search list", "Print current list", "Generate new list", "Exit"], title="\nWhat would you like to do?").show()

        if sort_or_search == 0:
            sort_choice = TerminalMenu(
                ["Bubble Sort", "Selection Sort", "Insertion Sort", "Quick Sort"], title="\nWhat sorting algorithm would you like to use?").show()
            if sort_choice == 0:
                algos.bubbleSort()
            elif sort_choice == 1:
                algos.selectionSort()
            elif sort_choice == 2:
                algos.insertionSort()
            else:
                algos.quicksort()

        elif sort_or_search == 1:

            target = input("Please input a target value for searching: ")

            target = int(target) if listType == "numeric" else target

            search_choice = TerminalMenu(
                ["Linear search", "Binary search"], title=f"Thanks! What searching algorithm would you like to use to find {target}?").show()
            if search_choice == 0:
                algos.linearSearch(target)
            else:
                algos.binarySearch(target)
        elif sort_or_search == 2:
            algos.printList()
        elif sort_or_search == 3:

            list_type = TerminalMenu(
                ["Numeric list", "Word list"], title="What kind of list would you like to generate?").show()

            listType = "numeric" if list_type == 0 else "word"

            size = input(
                "What size list? Please enter a positive integer: ")
            try:
                size = int(size)
            except ValueError:
                print("That's not an integer! Play nice or leave!")
                return exit()

            if list_type == 0:
                algos.generateNumericList(size)
            else:
                algos.generateWordList(size)
        else:
            print("goodbye!")
            exit()


if __name__ == "__main__":
    main()
