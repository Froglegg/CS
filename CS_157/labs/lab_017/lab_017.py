from directoryMethods import *


def main():
    while True:
        menu()
        choice = int(input("Enter Menu Choice Now! "))

        if (choice == 1):
            empFile = open("employees.txt", "r")
            for line in empFile:
                tokens = line.split(" ")
                print(tokens[0], "", tokens[1], "",
                      (float(tokens[2]) * float(tokens[3])))

        if (choice == 2):
            name = input("Enter a name to search an employee ")
            emp = findEmployee(name)
            if not emp:
                print("employee not found!")
            else:
                print(f"{emp[1][0]} {emp[1][1]}")

        if (choice == 3):
            createEmployee()

        if (choice == 4):
            name = input(
                "Enter the name of the employee you want to delete (First Last): ")
            deleteEmployee(name)

        if (choice == 5):
            name = input(
                "Enter the name of the employee you want to update (First Last): ")
            updateEmployee(name)
        if (choice == 6):
            print("\nGoodbye!")
            break
            exit()


if __name__ == "__main__":
    main()
