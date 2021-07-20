from simple_term_menu import TerminalMenu
from classes import Product, Asset


def navigateBatch(batch: Asset):

    prev_asset_stack = []

    def recursiveNavigation(asset: Asset, prevAsset: Asset or None = None):

        if prevAsset:
            prev_asset_stack.append(prevAsset)

        print(
            f"\n ~*~*~*~* Viewing {asset.getTag()} ({asset.getUnitOfMeasure()}) Children ~*~*~*~ \n")
        print(asset.getAssetTable()
              if asset.assetChildren else "No children to view")

        while True:

            options = list(filter(lambda item: item is not None, ["View Children",
                                                                  "View Child Asset" if asset.assetChildren else None, "View Parent Asset" if prevAsset else None, "View Event Log", "Update Event Log", "Exit"]))

            entry = TerminalMenu(options,
                                 title=f"\nWhat would you like to do with {asset.getTag()}?").show()

            if options[entry] == "View Children":
                print(
                    f"\n ~*~*~*~* Viewing {asset.getTag()} ({asset.getUnitOfMeasure()}) Children ~*~*~*~ \n")
                print(asset.getAssetTable())
                pass

            if options[entry] == "Update Event Log":
                print(
                    f"\nUpdating event log for {asset.getTag()}. \nNOTE: Updates are recursive and will update the event log for all of this assets' children, as well.")
                event = input(
                    str("Please enter an event (e.g., Lost, Damaged, Arrived at Location, Scan): "))
                asset.updateEventLog(event)
                print("Update success!")
                pass

            if options[entry] == "View Event Log":
                print(
                    f"\n ~*~*~*~* Viewing {asset.getTag()} ({asset.getUnitOfMeasure()}) Event Log ~*~*~*~ \n")
                print(asset.getEventLogTable())
                pass

            if options[entry] == "View Child Asset":
                asset_li = asset.getListIterator()
                asset_li.first()
                items = [asset_li.next() for i in range(len(asset))]
                entry = TerminalMenu([i.getTag() for i in items],
                                     title="\nWhich child asset would you like to view?").show()
                assetToView = items[entry]
                recursiveNavigation(assetToView, asset)
                break
            if options[entry] == "View Parent Asset":

                recursiveNavigation(prev_asset_stack.pop(), prev_asset_stack.pop() if len(
                    prev_asset_stack) > 0 else None)
                break

            if options[entry] == "Exit":
                break

    return recursiveNavigation(batch)


def createBatch():
    batch_name = str(input("\nEnter a name for your batch: "))

    product = Product(str(input("\nWhat product is in the batch?: ")))

    palletCount = int(
        input("How many pallets in the batch? Integer only: "))

    caseCount = int(
        input("How many cases per pallet? Integer only: "))

    itemCount = int(
        input("How many items per case? Integer only: "))

    # recursive list comprehension builds a linked list of linked lists... this is our asset hierarchy
    batch = Asset(product, "batch", [Asset(product, "pallet", [Asset(product, "case", [Asset(product, "item", None, tag=f"{product}-{pallet+1}-{case+1}-{item+1}")
                                                                                       for item in range(itemCount)], tag=f"{product}-{pallet+1}-{case+1}") for case in range(caseCount)], tag=f"{product}-{pallet + 1}") for pallet in range(palletCount)], tag=batch_name)
    return batch


def main():
    ''' 
        Topologies.py is a proof of concept application that allows warehouse managers to create digital representations of assets and collections of assets, called "batches"

        Nomenclature: An "asset" is a unit of measure of a "product". "Batches" are collections of "assets", called "units of measure"

        Assets come in three hierarchical units of measure: Pallets, Cases, and Items

        The hierarchical units of measure have parent/child relationships. Each asset has assetChildren, except for items. 

        Each asset has an "event log" that consists of several date/time and an event such Arrive at Location, Damaged, Lost

        Updates to the event log are recursive and traverse hierarchies from the top down, so that e.g. an update to a Pallet will update all cases and items within that pallet, but will not update cases and items within the other pallet, etc.

        Users of this proof-of-concept can do the following:
        - Create batches, navigate batch hierarchies, and delete batches 
        - Update event log for batch or asset in a batch
        - View event log for batch or asset in a batch
    '''
    print("\n~*~*~* Welcome to Topologies, a warehouse management tool. ~*~*~*~*\n")
    batches = []

    while True:
        entry = TerminalMenu(["Create a batch", "View batch", "Delete a batch",
                              "Exit"], title="\nWhat would you like to do?").show()

        if entry == 0:
            batch = createBatch()
            batches.append(batch)
            print(f"\n{batch.getTag()} batch created! Top level of batch is: \n")
            print(batch.getAssetTable())

        elif entry == 1:
            if len(batches) <= 0:
                print("No batches created yet!")
            else:
                batch_to_view = TerminalMenu(
                    [i.getTag() for i in batches], title="\nWhich batch would you like to view?").show()
                print(
                    f"\nViewing {batches[batch_to_view].getTag()}, created at {batches[batch_to_view].getTimeCreated()}")

                navigateBatch(batches[batch_to_view])

        elif entry == 2:
            if len(batches) <= 0:
                print("No batches to delete!")
            else:
                batch_to_delete = TerminalMenu(
                    [i.getTag() for i in batches], title="\nWhich batch would you like to remove?").show()
                print(f"\nDeleting {batches[batch_to_delete].getTag()}")
                batches.pop(batch_to_delete)

        else:
            print("\nGoodbye!")
            exit()


if __name__ == "__main__":
    main()
