import numpy as np


def ScalarMult(ScaM, num):
    for i in range(len(ScaM)):
        for j in range(len(ScaM[0])):
            ScaM[i][j] = num * ScaM[i][j]
    return ScaM


def MatrixAdd(Matrix1, Matrix2):

    for i in range(len(Matrix1)):
        for j in range(len(Matrix1[0])):
            Matrix1[i][j] = Matrix1[i][j] + Matrix2[i][j]
    return Matrix1


def MatrixSubtract(Matrix1, Matrix2):
    for i in range(len(Matrix1)):
        for j in range(len(Matrix1[0])):
            Matrix1[i][j] = Matrix1[i][j] - Matrix2[i][j]
    return Matrix1


def MatrixMultiply(Matrix1, Matrix2):
    for i in range(len(Matrix1)):
        for j in range(len(Matrix1[0])):
            Matrix1[i][j] = Matrix1[i][j] * Matrix2[i][j]
    return Matrix1


def MatrixTranspose(Matrix):
    transposedMatrix = [[] for i in range(len(Matrix))]
    for row in Matrix:
        for idx, item in enumerate(row):
            transposedMatrix[idx].append(item)
    return transposedMatrix


def AnalyzeTranspose(Matrix):
    transposedMatrix = MatrixTranspose(Matrix)
    return MatrixSubtract(Matrix, transposedMatrix)


def MatrixDeterminant(Matrix):
    return np.linalg.det(Matrix)


def MatrixTrace(Matrix):
    return np.trace(Matrix)
