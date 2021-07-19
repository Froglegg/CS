from simple_term_menu import TerminalMenu
from tabulate import tabulate
from classes import Product, Asset, Batch


def main():
    ''' Topologies.py is a proof of concept application that allows warehouse managers to create digital representations of assets and collections of assets, called "batches"
        Nomenclature: An "asset" is a unit of measure of a "product". "Batches" are collections of "assets", called "units of measure"
        Assets come in three hierarchical units of measure: Pallets, Cases, and Items
        The hierarchical units of measure have parent/child relationships.
        Each asset has an "event log" that consists of several date/time and an event such Arrive at Location, Damaged, Lost
        Updates to the event log traverse hierarchies from the top down, so that e.g. an update to a Pallet will update all cases and items
        Users of this proof-of-concept can do the following:
        - Create, read, and delete batches 
        - Update event log for batch or asset in a batch
        - View event log for batch or asset in a batch

        TODO: Enable a "count" feature for units of measure, so that n pallets can have n cases, and n cases can have n items
        TODO: Create a linked list for each pallet in a count, with pointers to the pallets' cases, and pointers from each case to the cases' items
        TODO: Create navigation feature for exploring each branch of an asset and its children using a list iterator
        TODO: Create logic for updating event log for assets so that updates to an asset will propagate to that assets' children
    '''
    print("\n~*~*~* Welcome to Topologies, a warehouse management tool. ~*~*~*~*\n")
    batches = []

    while True:
        entry = TerminalMenu(["Create a batch", "View batch", "Delete a batch",
                              "Update event log", "View event log", "Exit"], title="\nWhat would you like to do?").show()
        if entry == 0:
            batch_name = str(input("\nEnter a name for your batch: "))
            product = Product(str(input("\nWhat product is in the batch?: ")))

            pallet = Asset(product, "pallet", int(
                input("How many pallets? Integer only: ")))

            case = Asset(product, "case", int(
                pallet.getBatchCount() * input("How many cases per pallet? Integer only: ")))

            item = Asset(product, "item", int(
                case.getBatchCount() * input("How many items per case? Integer only: ")))

            palletList = [pallet for i in range(pallet.getBatchCount())]
            caseList = [case for i in range(case.getBatchCount())]
            itemList = [item for i in range(item.getBatchCount())]

            batch = Batch([pallets, cases, items], batch_name)
            batches.append(batch)
            print(f"\n{batch.getName()} batch created!\n")
            print(batch.getBatchTable())

        elif entry == 1:
            if len(batches) <= 0:
                print("No batches created yet!")
            else:
                batch_to_view = TerminalMenu(
                    [i.getName() for i in batches], title="\nWhich batch would you like to view?").show()
                print(
                    f"\nViewing {batches[batch_to_view].getName()}, created at {batches[batch_to_view].getTimeCreated()}")
                print(batches[batch_to_view].getBatchTable())
        elif entry == 2:
            if len(batches) <= 0:
                print("No batches to delete!")
            else:
                batch_to_delete = TerminalMenu(
                    [i.getName() for i in batches], title="\nWhich batch would you like to remove?").show()
                print(f"\nDeleting {batches[batch_to_delete].getName()}")
                batches.pop(batch_to_delete)
        elif entry == 3:
            if len(batches) <= 0:
                print("No batches to update!")
            else:

                batch_to_update = TerminalMenu([i.getName(
                ) for i in batches], title="\nWhich event log would you like to update?").show()
                selectedBatch: Batch = batches[batch_to_update]
                asset_to_update = TerminalMenu([i.getUnitOfMeasure(
                ) for i in selectedBatch], title="\nWhich unit of measure would you like to update?").show()

                event = str(input(
                    "What event would you like to add to the log? E.g., 'Lost', 'Arrived at Location', 'Damaged', etc.: "))

                selectedBatch.updateEventLog(event, asset_to_update)

                print("Success! Updated event log: \n")
                print(selectedBatch.getEventLogTable())

        elif entry == 4:
            batch_to_view = TerminalMenu([i.getName(
            ) for i in batches], title="\nWhich event log would you like to view?").show()
            selectedBatch: Batch = batches[batch_to_view]
            print("")
            print(selectedBatch.getEventLogTable())
        else:
            print("\nGoodbye!")
            exit()


if __name__ == "__main__":
    main()
