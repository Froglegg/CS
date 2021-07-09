from priority_linked_queue import Comparable, PriorityLinkedQueue
from simple_term_menu import TerminalMenu
from tabulate import tabulate
from random import choice
import json

# priority is given in this queue to items that take very little time to make, e.g., fries and milkshakes, as opposed to cheeseburgers and cookout trays
# the queue is constructed by passing in a number of these items and then popping them out in order of priority and time spent in the queue
menuDict = {
    "fries": 1,
    "milkshake": 1,
    "cheeseburger": 2,
    "hotdog": 2,
    "chilidog": 3,
    "chicken tenders": 3,
    "cookout tray": 4,
    "party tray": 5
}

menuTable = tabulate([
                     [key, value] for key, value in menuDict.items()], headers=["Menu Item", "Priority (ordinal speed)"], tablefmt='github', numalign="left")


def main():
    print("~*~*~*~ Welcome to Cookout Queue Simulator! ~*~*~*~*~")
    print("Menu (quicker items get first priority in queue):\n")
    print(menuTable)

    while True:
        customer_queue = None

        entry = TerminalMenu(["Generate queue", "Exit"],
                             title="\nWhat would you like to do?").show()
        if entry == 0:

            number_of_customers = int(input(
                "\nHow many customers in line?: "))
            print(
                "\nGenerating random orders and inserting them into appropriate position in queue...")
            sourceCollection = []
            for i in range(number_of_customers):
                randomChoice = choice(
                    list(menuDict.items()))
                comparable = Comparable(
                    f"Customer #{i+1}: {randomChoice[0]}", randomChoice[1])
                sourceCollection.append(comparable)

            customer_queue = PriorityLinkedQueue(sourceCollection)

            print(
                f"\nPrioritized order queue for {len(customer_queue)} customer(s) created. The bottom most customers are first in line, as their orders are fastest to make!")
            for i in customer_queue:
                print(i.getData())

            while True:
                if customer_queue.isEmpty():
                    print("\nThe queue is empty!")
                    break
                run_queue = TerminalMenu(
                    ["View Queue", "Peek", "Serve an order", "Simulate Dequeue", "Nothing"], title="\nWhat would you like to do with this queue?").show()

                if run_queue == 0:
                    print("")
                    for i in customer_queue:
                        print(i.getData())
                elif run_queue == 1:
                    print(
                        f"\nFirst up in the queue is: {customer_queue.peek()}")
                elif run_queue == 2:
                    print(f"\nOrder up!: {customer_queue.dequeue()}")
                elif run_queue == 3:
                    print("\nDequeing each order until the queue is empty...\n")
                    while not customer_queue.isEmpty():
                        print(f"\nOrder up!: {customer_queue.dequeue()}")
                else:
                    break

        else:
            print("\nGoodbye!")
            exit()


if __name__ == "__main__":
    main()
