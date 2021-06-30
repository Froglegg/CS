from random import randint
from tabulate import tabulate
import pickle


class List2D(object):
    ''' 2d List with the first column in each row containing the number of the row, used in Library class to indicate the floor of the library '''

    def __init__(self, rows, columns) -> any:
        super().__init__()
        self.data = [i for i in range(rows)]
        # first item will be idx + 1, or, the row number
        for row in range(rows):
            self.data[row] = [
                None for i in range(columns)]
        return self.data

    def __str__(self):
        return str(self.data)


class Library(List2D):
    '''
    Library Class Accepts rows, columns and genres as arguments and builds a multidimensional list representing a library
    Two empty 2D lists are initialized with row x column dimensions, these represent the library categories matrix and the library quantities matrix
    Library categories and library quantities matrices are cross referenced by using a genre dictionary, whose keys (ints) are referenced in the library categories matrix. 
    The position of the genre key in the library category matrix is cross-referenced with the library quantity matrix to produce a meaningful representation of how many items of each genre category are in each position (room) in the library matrix
    '''

    def __init__(self, rows, columns,  genres) -> None:

        self.libraryQuantities = super().__init__(rows, columns)
        self.libraryCategories = super().__init__(rows, columns)
        self.library = super().__init__(rows, columns)

        self.rows = rows
        self.columns = columns
        self.genres = genres
        self.genreKeys = [k for k in genres.keys()]

        # construct library categories matrix
        for row in range(len(self.libraryCategories)):
            # assign random integer from genre keys for each column in row
            for col in range(len(self.libraryCategories[row])):
                self.libraryCategories[row][col] = randint(
                    self.genreKeys[0], self.genreKeys[(len(self.genreKeys) - 1)])

        # construct library quantities matrix
        for row in range(len(self.libraryQuantities)):
            # assign random integer between 1 and 50 for each column in row
            for col in range(len(self.libraryQuantities[row])):
                self.libraryQuantities[row][col] = randint(
                    1, 50)

        # build multidimensional library by combining the two lists and cross referencing genre keys
        for row in range(len(self.library)):
            # assign random integer for each column in row, skipping the first column at index 1, which holds the row number...
            for col in range(len(self.library[row])):
                self.library[row][col] = [genres[self.libraryCategories[row]
                                                 [col]], self.libraryQuantities[row][col]]

    def getCategoryMatrix(self):
        return self.libraryCategories

    def getQuantitiesMatrix(self):
        return self.libraryQuantities

    def getLibrary(self):
        return self.library

    def getTable(self):
        '''return dynamic, tabular representation of data'''

        return tabulate(self.getLibrary(), headers=["Floor"] + [f"Room {i + 1}" for i in range(self.columns)], showindex=[(i + 1) for i in range(len(self.getLibrary()))])

    def saveLibrary(self):
        pickle.dump(self, open("library.p", "wb"))


availableSeats = [["x", "x", "o"], ["o", "o", "x"], ["x", "x", "x"]]
