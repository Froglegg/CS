from Library_Class import Library
from simple_term_menu import TerminalMenu
import pickle


def main():
    # a dictionary of genres
    genres = {1: "hobby", 2: "romance", 3: "cooking", 4: "science",
              5: "adventure", 6: "puzzles"}
    lib = None

    print("\n~*~*~*~* Welcome to the library simulator! ~*~*~*~\n")
    while True:
        new_library = TerminalMenu(
            ["Create new Library", "Load library", "Exit"], title="What would you like to do?").show()

        if new_library == 0:
            lib = Library(4, 4, genres)
            print("Library created.\n")
            break
        elif new_library == 1:
            try:
                lib = pickle.load(open("library.p", "rb"))
                print("Library loaded.\n")
                break
            except:
                print("No library saved! Create a new library to get started.\n")
        else:
            print("Goodbye!")
            exit()

    print(lib.getTable() + '\n')

    library = lib.getLibrary()

    while True:
        selection = TerminalMenu(
            ["Inspect room", "Save Library", "Exit"], title="What would you like to do?").show()

        if selection == 0:
            select_floor = TerminalMenu([f"Floor {i + 1}" for i in range(
                len(library))], title="What floor would you like to inspect?").show()

            select_room = TerminalMenu(
                [f"Room {i +1}" for i in range(len(library[select_floor]))], title=f"What room on floor {select_floor +1}").show()
            print(
                f"\nRoom {select_room + 1} on floor {select_floor + 1} has {library[select_floor][select_room][1]} {library[select_floor][select_room][0]} magazines\n")
        elif selection == 1:
            try:
                print("saving library...")
                lib.saveLibrary()
                print("Library saved!\n")
            except:
                print("Uh-oh! Was unable to save library! Bad developer!\n")
        else:
            print("goodbye!")
            exit()


if __name__ == "__main__":
    main()
