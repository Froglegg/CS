from itertools import combinations


class Library(dict):
    '''
    Hashable library class
    We could just use a dict of dicts, but I'm a fan of descriptive OOP
    '''

    def __init__(self, sourceCollection=None):
        self.bookCollection = []
        if sourceCollection:
            self.bookCollection = sourceCollection
            for book in sourceCollection:
                self.add(book)

    def add(self, book):
        self.bookCollection.append(book)
        self[book["name"]] = book

    def __hash__(self):
        return hash(tuple(self.bookCollection))


class Book(dict):
    def __init__(self, name, weight, value) -> None:
        super().__init__()
        self["name"] = name
        self["weight"] = weight
        self["value"] = value

    def __hash__(self):
        return hash((self["name"], self["weight"], self["value"]))


def knapsack(maxWeight=10, library=Library()) -> tuple:
    '''
    This iterative knapsack algorithm takes in a maxWeight integer and a collection of books (a Library), 
    and outputs the best possible combination of books with a maximum value that is not greater than the maxWeight value.

    It does so by iterating through the range r, which is the size of the library, producing 
    successive r-length combinations (sets of non-repeating permutations) using itertools.combinations,
    summing the total weights and values of each combination and returning the best combination in terms of weight and value.

    Worst-case complexity: Quadratic O(n^2), where n is the number of books in the library

    Justification: Because we must examine r-length sets of 
    n books, where r is [len(n)...0] and n is len(books), we must iterate n^2 times. 
    '''
    # scope out and initialize global variables
    global bestValue, bestCombo
    bestValue = 0
    bestCombo = ()

    # iterate backwards through the range [len(library)...0], testing r-length combinations of books
    # stepping backwards through the library will begin with the greatest number of books, first.
    for r in range(len(library), 0, -1):
        # nested iteration, for each r-length combination of books
        for comb in combinations(library.items(), r):
            # sum total weight of books
            totalWeight = sum([tup[1]["weight"] for tup in comb])
            # sum total value of books
            totalValue = sum([tup[1]["value"] for tup in comb])
            # if total weight is not greater than max weight and totalValue is not less than best value
            if totalWeight <= maxWeight and totalValue >= bestValue:

                # set global variables for bestValue and bestCombo
                bestValue = totalValue
                bestCombo = comb
                # return tuple of best book collection and its summed value
                return (bestCombo, bestValue)


def main():
    weight_of_knapsack = 0
    number_of_items = 0
    library = Library()

    print("\n~*~*~*~ Knapsack Problem ~*~*~*~*\n")
    print("You are a well-known, ambitious, and rich book collector in Ancient Athens, trying to expand your library by any means necessary.\nYou've recently been introduced to a skilled cat burglar who has offered his services to you, however, he has only so much room in his knapsack and can only steal so many books for you.\nHe needs a list of all the books you might want, as well as their weights and estimated market value, so that he can make the best possible heist.")
    print("Aristotle and a time travelling computer programmer named Hayes Crowley have worked together to write you a program to help you craft this list. All you need to do is follow the instructions below (note: Please use integers for all inputs!)\n")
    print("~*~*~*~~*~* Begin User Input ~*~*~*~*~*~*\n")

    while True:
        try:
            weight_of_knapsack = int(
                input("How much weight can the knapsack carry?: "))
            number_of_items = int(
                input("How many books are you trying to acquire?: "))

            if number_of_items <= 1:
                print("Please enter more than one book!")
                exit()

            for item in range(number_of_items):

                name = input(
                    f"Please enter the name of book {item + 1} (leave empty to use book number): ") or item + 1

                weight = int(
                    input(f"Please enter the weight of book {name}: "))
                value = int(input(
                    f"Please enter the value if book {name} (in drachmas): "))
                library.add(Book(name, weight, value))

            print("~*~*~*~ Output ~*~*~*~")
            bestCombo, totalValue = knapsack(weight_of_knapsack, library)
            print("Best book combination: ")
            print(bestCombo)
            print("Total Value: ")
            print(f'{totalValue} drachmas')
            break
        except ValueError:
            print("Please enter an integer!")


if __name__ == "__main__":
    main()
