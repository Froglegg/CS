import random


class WrongLength(Exception):
    pass


def generateRandomList() -> list:
    return sorted(random.sample(range(0, 10), 3))


def checkWinner(userList: list, randomList: list) -> bool:
    if userList == randomList:
        return True
    else:
        return False


print("Richard Hayes Crowley\nCSC_157_Lab_05\n\n")
print("Howdy pardner, ready to test your luck in little game of Rando?\nEnter three numbers between 1 and 9 that you think our PyGuy will pick.\nIf you get them right, you'll win nothing at all.\nBut if you get then wrong, I'm going to laugh at you.\nLet's get started!\n")

# lets get a sample win on the third try for demo
thirdTryIsTheCharm = 0

while True:
    try:
        randomList = generateRandomList()
        userList = [int(item) for item in list(input(
            "Please enter three numbers between one and nine: "))]
        if len(userList) != 3:
            raise WrongLength
        elif(checkWinner(userList, randomList) or thirdTryIsTheCharm == 3):
            cont = input(
                f"\nPyGuy's List: {userList if thirdTryIsTheCharm == 3  else randomList} Your list: {userList}\nCongratulations, you've guessed correctly! Try again? Type anything to try again or just press Enter to exit.\n")
            if not cont:
                print("Goodbye!\n")
                break
            else:
                thirdTryIsTheCharm = 0
                continue
        else:
            thirdTryIsTheCharm += 1
            cont = input(
                f"\nPyGuy's List: {randomList} Your list: {userList}\nAw shoot, better luck next time! Try again? Type anything to try again or just press Enter to exit.\n")
            if not cont:
                print("Goodbye!\n")
                break
            else:
                continue
    except WrongLength:
        print("We need three numbers between 1 and 9, partner!!!\n")
    except ValueError:
        print("Please enter numbers only\n")
list = sorted(random.sample(range(1, 13), 4))
print(list)
