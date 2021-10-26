# Richard Hayes Crowley
# MAT_144_project_1
# Chapter 5, question 9

# 9. Given a list of integers and an element x,
# locate x in this list using a recursive implementation of linear search.

from random import randint


def recursive_linear_search(index, stop, x, lyst):
    if lyst[index] == x:
        return index
    elif index == stop:
        raise Exception("Item not found!")
    return recursive_linear_search(index + 1, stop, x, lyst)


def main():
    lyst = [randint(0, 100) for _ in range(10)]
    searchTerm = None

    print("Recursive linear search")
    print(f"List: {lyst}")

    while True:
        try:
            searchTerm = int(input("Please enter an integer to search for: "))
            break
        except ValueError:
            print("Please enter a valid integer to search for!")

    print(f"\nSearching for {searchTerm} in {lyst}\n")

    try:
        indexOfSearchTerm = recursive_linear_search(
            0, len(lyst)-1, searchTerm, lyst)
        print(
            f"Item found! Index of search term {searchTerm} is {indexOfSearchTerm} in {lyst}")
    except:
        print(f"{searchTerm} not found in {lyst}!")


if __name__ == "__main__":
    main()
