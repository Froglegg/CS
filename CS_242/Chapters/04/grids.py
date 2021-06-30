# two dimensional arrays are grids
from arrays import Array


class Grid(object):
    """2d grid or matrix"""

    def __init__(self, rows, columns, fillValue=None) -> None:
        super().__init__()
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fillValue)

    def getHeight(self):
        ''' returns number of rows'''
        return len(self.data)

    def getWidth(self):
        '''return number of columns'''
        return len(self.data[0])

    def __getitem__(self, index):
        '''support 2d indexing with [row][column]'''
        return self.data[index]

    def __str__(self) -> str:
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return result


grid = Grid(5, 5)
print(grid)


class Grid3D(Grid):
    ''' 3d grid'''

    def __init__(self, rows, columns, depth, fillValue=None) -> None:
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)
            for d in range(len(self.data[row])):
                self.data[row][d] = Array(depth, fillValue)

    def getDepth(self):
        return len(self.data[0][0])

    def __str__(self) -> str:
        result = ""
        for row in range(self.getHeight()):
            result += "["
            for col in range(self.getWidth()):
                result += "[ "
                for d in range(self.getDepth()):
                    result += str(self.data[row][col][d]) + " "
                result += "]"
            result += "]\n"
        return result


three_d_grid = Grid3D(3, 3, 3,)
print(three_d_grid)
