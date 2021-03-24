# Richard Hayes Crowley
# 03/18/2020
# CSC_157_LAB_010
import json
from os import path
from pprint import pprint, pformat


class AncillaryException(Exception):
    """Custom exception for not entering 'y' or 'n' for ancillary CD ROM"""
    pass


class Inventory(object):
    # changing the structure of my class variable from a list to a dict, preload with previous JSON state if it exists
    # structure will use titles as keys, since titles must be unique, and title.author, title.description, title.ancillary as properties
    inventory = json.load(open("inventory.json", "r")) if path.exists(
        "inventory.json") else {}

    def __init__(self, title, description):
        # setting title as key for another dict which will hold description as a key/value pair
        Inventory.inventory[title] = {"description": description}

    @staticmethod
    def inventoryCheck(title):
        return title in Inventory.inventory
        # check if the title already exists in the list of titles


class Books(Inventory):
    def __init__(self, title, description, author, ancillary=None):
        # execute the parent constructor
        super().__init__(title, description)
        # setting author and ancillary for title in inventory
        Books.inventory[title]["author"] = author
        Books.inventory[title]["ancillary"] = True if ancillary == "y" else False

    def get_inventory():
        return Books.inventory

    def __str__(self):
        current_stock = json.load(open("inventory.json", "r")) if path.exists(
            "inventory.json") else self.inventory
        # format dict to prettified string
        return pformat(current_stock)


oscar = Books("An Ideal Husband",
              "Wilde's scintillating drawing-room comedy ", "Oscar Wilde")

title_to_check = input("Title to check in inventory: ")

if (Books.inventoryCheck(title_to_check)):  # perform a check
    print("The title already exists; it cannot be added to the inventory.")
else:
    print('"' + title_to_check + '" does not exist in inventory.')
    print('Enter information about "' + title_to_check + '":\n')
    author = input("Author of book: ")
    description = input("Description of book: ")
    while True:
        try:
            ancillary = input(
                "Does this book come with a CD-ROM? Enter y or n: ")
            if ancillary != "y" and ancillary != "n":
                raise AncillaryException

        except AncillaryException:
            print("Please enter either 'y' or 'n'")
        else:
            break

    updated_inventory = Books(title_to_check, description, author,
                              ancillary if ancillary == "y" else None)

    # add the updated inventory book to json
    json.dump(Books.get_inventory(), open("inventory.json", "w"),
              indent=4, sort_keys=True)

    print('\n"' + title_to_check + '" has been added to the inventory.\n')

    print(f"Inventory to date is: {updated_inventory}")
