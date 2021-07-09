from arrayBag import ArrayBag
from linkedBag import LinkedBag
from simple_term_menu import TerminalMenu

groceriesDict = {"Fruits": 1.50, "Eggs": 2.50, "Cereal": 4, "Milk": 4.00,
                 "Bread": 3.95, "Meats": 8.25, "Cheeses": 6.75, "Vegetables": 3.25}

groceriesList = list(groceriesDict.keys())

groceriesInventory = [
    f"{value[0]}: ${value[1]:.02f}" for value in groceriesDict.items()]


def main():
    global groceriesDict
    ''' 
    Shopping Bag uses two different "bag" data structures (a linkedBag and a dynamic arrayBag)

    The user can choose between using a linkedBag or an arrayBag

    The array Bag is dynamically sized, e.g., a new array of a greater or lesser length is created whenever a certain threshold (or, "load factor") is reached. This is described in the ArrayBag class code.

    In this program, the user can: 
    •	Open a bag to be utilized

    •	Add contents to the bag

    •	Remove an item from the bag

    •	Check if an item is contained within the bag

    •	Clear their bag

    •	Check out (run a sum function to find price of all items in bag)

    '''

    print("Welcome to the Shopping bag app! Let's get some groceries!")

    bag = None

    entryPoint = TerminalMenu(["Array Bag", "Linked Bag", "Exit"],
                              title="What kind of shopping bag would you like to use?").show()

    if entryPoint == 0:
        print("You chose Array Bag")

        bag = ArrayBag()
        goShopping(bag)
    elif entryPoint == 1:
        print("You chose Linked Bag")

        bag = LinkedBag()
        goShopping(bag)
    else:
        print("Goodbye!")
        exit()


def goShopping(bag):
    global groceriesDict
    global runningTotal
    print(
        f"Let's go shopping!\nHere are the groceries and their prices: {[i for i in groceriesInventory]}")

    while True:
        option = TerminalMenu(["View bag", "Add items to bag", "Remove items from bag",
                               "Check if item is in bag", "Empty Bag", "Checkout", "Exit"], title="What would you like to do?").show()
        if(option == 0):
            print([f"{i}" for i in bag])
        elif(option == 1):
            item_to_add = TerminalMenu(
                groceriesList, title="What item would you like to add to your bag?").show()
            bag.add(groceriesList[item_to_add])
            print(bag)

        elif(option == 2):
            if bag.isEmpty():
                print("Nothing to remove!")
            else:
                item_to_remove = TerminalMenu(
                    [item for item in bag], title="Which item would you like to remove?").show()
                item_to_remove = [item for item in bag][item_to_remove]
                bag.remove(item_to_remove)
                print(bag)

        elif(option == 3):
            item_to_check = TerminalMenu(
                groceriesList, title="What item would you like to check in your bag?").show()
            checkItem = groceriesList[item_to_check] in bag
            if checkItem:
                print(f"{groceriesList[item_to_check]} is in your bag!")
            else:
                print(f"{groceriesList[item_to_check]} is NOT in your bag!")

        elif(option == 4):
            bag.clear()
            print(f"Bag cleared!")

        elif(option == 5):
            print(f"Checking out! Items in bag: {[f'{i}' for i in bag]}")
            runningTotal = sum([groceriesDict[i] for i in bag])
            print(f"Your total is: ${runningTotal:0.2f}")
            print("Goodbye!")
            exit()

        else:
            print("Goodbye!")
            exit()


if __name__ == "__main__":
    main()
