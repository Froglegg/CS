class MatrixMultiplicationError(Exception):
    def __str__(self):
        return "The two matrices you're trying to multiply have inconsistent shapes."
        

def transpose(matrix):
     numberOfCols = len(matrix[0])
     test = all(map(lambda row: len(row) == numberOfCols, matrix))
     if test:
         return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
     else:
         raise MatrixMultiplicationError


def dotProduct(vector1, vector2):
    def dotProductHelper(vec1, vec2):
        if len(vec1) != len(vec2):
            raise MatrixMultiplicationError
        else:
            if not(bool(vec1)) and not(bool(vec2)):
                return 0
            else:
                return vec1[0] * vec2[0] + dotProductHelper(vec1[1:], vec2[1:])
    return dotProductHelper(vector1, vector2)


def matrixMultiply(matrix1, matrix2):
    try:
        return transpose([[dotProduct(matrix1Row, matrix2Row) for matrix1Row in matrix1]
                          for matrix2Row in transpose(matrix2)])
    except MatrixMultiplicationError as e:
        print()
        print(e)





