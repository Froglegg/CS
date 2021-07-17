from LinkedList.LinkedList import LinkedList
from simple_term_menu import TerminalMenu
from tabulate import tabulate


def create_product():
    pass


def create_batch():
    pass


def update_event_log(asset):
    pass


def view_event_log(asset):
    pass


def main():
    ''' Topologies.py is a proof of concept application that allows warehouse managers to create digital representations of assets and collections of assets, called "batches"
        Nomenclature: An "asset" is a unit of measure of a "product". "Batches" are collections of "assets", called "units of measure"
        Assets come in three hierarchical units of measure: Pallets, Cases, and Items
        The hierarchical units of measure have parent/child relationships, so that a batch can have n Pallets, and pallets can have n Cases, which can have n Items, etc.
        Each asset has an "event log" that consists of several date/time and an event: Origin, Arrive at Location, Damaged, Lost
        Updates to the event log traverse hierarchies from the top down, so that e.g. an update to a Pallet will update all cases and items within those cases.
        Users of this proof-of-concept can do the following:
        - CRUD products
        - CRUD batches
        - Update event log for batch or asset in a batch
        - View event log for batch or asset in a batch
    '''
    print("\nWelcome to Topologies, a warehouse management tool.")

    pass


if __name__ == "__main__":
    main()
