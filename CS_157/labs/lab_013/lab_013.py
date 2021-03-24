# program to add manipulate 3 by 3 matrices using nested loops
# Richard Hayes Crowley, CSC_157, 03-22-2021
import operations as matrix_utils

global continue_program


def main():
    class OptionException(Exception):
        """Custom exception for not choosing correct option"""
        pass

    continue_program = True
    # original matrices
    MatX = [[9, 11, 4], [3, 10, 4], [6, 7, 11]]
    MatY = [[3, 9, 2], [1, 9, 6], [10, 2, 4]]

    def showMatrix(MatA, m, n):
        for i in range(m):
            for j in range(n):
                try:
                    print(MatA[i][j], "\t", end="")
                except IndexError:
                    print(
                        "Out of range, are you sure you inputted the correct rows / columns length?")
            print("\n")
        # Matrix X
    print("---------------------")
    print("Matrix X")
    print("---------------------")
    showMatrix(MatX, 3, 3)
    print(" ")
    # Matrix Y
    print("---------------------")
    print("Matrix Y")
    print("---------------------")
    showMatrix(MatY, 3, 3)

    optionsDict = {
        "test": print,
        "a": matrix_utils.ScalarMult,
        "b": matrix_utils.MatrixAdd,
        "c": matrix_utils.MatrixMultiply,
        "d": matrix_utils.MatrixTranspose,
        "e": matrix_utils.AnalyzeTranspose,
        "f": matrix_utils.MatrixDeterminant,
        "g": matrix_utils.MatrixTrace
    }

    while continue_program:

        # Scalar Multiplication
        print("---------------------")
        print("Please choose an operation to perform on a matrix or matrices (or type Q to quit): ")
        print("---------------------")
        option = ""
        while True:
            try:
                option = input(
                    "A) Scalar Multiply\nB) Matrix Add \nC) Matrix Multiply \nD) Matrix Tranpose \nE) Analyze Transpose  \nF) Matrix Determinant \nG) Matrix Trace\n\rChoice: ").lower()
                if option == "q":
                    break
                elif option not in ["a", "b", "c", "d", "e", "f", "g"]:
                    raise OptionException
                else:
                    break
            except OptionException:
                print(
                    "Please input one of the following or else type 'Q' to quit: A, B, C, D, E, F, G")

        if option == "q":
            print("Goodbye!")
            continue_program = False

        elif option.lower() == "a":
            while True:
                try:
                    mChoice = input(
                        "Which matrix would you like to scale?  A) MatrixX or B) MatrixY. Type Q to quit.\nChoice: ").lower()
                    if mChoice == "q":
                        print("goodbye!")
                        continue_program = False
                        break
                    elif mChoice not in ["a", "b"]:
                        raise OptionException
                    scale = int(
                        input("Please input an integer to scale this matrix by.\nInteger: "))
                    print(optionsDict["a"](
                        MatX if mChoice == "a" else MatY, scale))
                    cont = input(
                        "Would you like to continue? Enter Y if so.").lower()
                    if cont != "y":
                        continue_program = False
                    break
                except OptionException:
                    print("Please select A or B (or type Q to quit).")
                except ValueError:
                    print("Please enter an integer.")

        elif option.lower() in ["b", "c"]:
            print(optionsDict[option](MatX, MatY))
            cont = input("Would you like to continue? Enter Y if so: ").lower()
            if cont != "y":
                continue_program = False

        elif option.lower() in ["d", "e", "f", "g"]:
            while True:
                try:
                    mChoice = input(
                        "Which matrix would you like to perform this operation on?  A) MatrixX or B) MatrixY. Type Q to quit.\nChoice: ").lower()
                    if mChoice == "q":
                        print("goodbye!")
                        continue_program = False
                        break
                    elif mChoice not in ["a", "b"]:
                        raise OptionException
                    else:
                        print(optionsDict[option](
                            MatX if mChoice == "a" else MatY))
                        cont = input(
                            "Would you like to continue? Enter Y if so.")
                        if cont.lower() != "y":
                            continue_program = False
                        break
                except OptionException:
                    print("Please select A or B (or type Q to quit).")


main()
