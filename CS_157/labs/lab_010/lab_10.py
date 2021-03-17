# Definitions: class Inventory and class Books

class Inventory(object):
    titles = []
    # list of titles
    descriptions = []
    # list of corresponding descriptions

    def __init__(self, title, description):
        Inventory.titles.append(title)
        # add the title to a list
        Inventory.descriptions.append(description)
        # add the description to a list

    @staticmethod
    def inventoryCheck(title):
        return title in Inventory.titles
        # check if the title already exists in the list of titles


class Books(Inventory):
    authors = []
    # list of corresponding authors

    def __init__(self, title, description, author):
        super().__init__(title, description)
        # execute the parent constructor
        Books.authors.append(author)
        # add the author to a list

# instantiate class object(s)


oscar = Books("An Ideal Husband",
              "Wilde's scintillating drawing-room comedy ", "Oscar Wilde")
# description from https://www.barnesandnoble.com/

title_to_check = input("Title to check in inventory: ")

if (Books.inventoryCheck(title_to_check)):  # perform a check
    print("The title already exists; it cannot be added to the inventory.")
else:
    print('"' + title_to_check + '" does not exist in inventory.')
    print('Enter information about "' + title_to_check + '":')
    author = input("Author of book: ")
    description = input("Description of book: ")
    new_book = Books(title_to_check, description, author)
    # add the new book to the inventory
    print('"' + title_to_check + '" has been added to the inventory.')
