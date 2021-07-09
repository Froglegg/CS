import random
import datetime
from simple_term_menu import TerminalMenu
from movie_script import MovieScript

# the movie text and sequences
seq = []
seq.append("opening teaser sequence")
seq.append("main titles with theme song")

seq.append("the plot unfolds")
seq.append("meeting with the superiors")
seq.append("the gadgets are issued")
seq.append("the mission begins")
seq.append("a romance ensues")
seq.append("thwarted but persistent")
seq.append("physical confrontation with the enemy")
seq.append("the enemy is defeated")
seq.append("the loose ends unfold")
seq.append("on to the next mission")

seq.append("subplot: the drone has launched")
seq.append("subplot: secret vampire society exposed")
seq.append("subplot: Tom Cruise skateboards on an airplane")

# timings for scenes
sceneTimings = []
for i in range(len(seq)-1):
    x = random.uniform(0.1, 0.5)
    # using datetime timeDelta package to
    time = str(datetime.timedelta(hours=x))[2:-7] + " mins"
    sceneTimings.append(time)

# actor list
actors = ["Tom Cruise: Vampire", "Tilda Swinton: Vampire", "Chris Rock: Detective", "Angelina Jolie: Archaeologist", "Seth Rogen: Gamer",
          "Christopher Walken: Psychic", "Whoopi Goldberg: Nun", "Adam Sandler: Football player", "Jennifer Lopez: Journalist"]

# searchable list of keywords
spy_movie_keywords = ["drone", "gadgets", "romance", "enemy", "Tom Cruise",
                      "thwarted", "meeting", "mission", "secret", "theme song"]


def searchKeywords(ms):
    ls = spy_movie_keywords
    ls.append("Go Back")
    while True:
        keyword = TerminalMenu(
            ls, title="\nWhat word would like to search for?").show()
        # "go back" option is last option
        if keyword == len(ls) - 1:
            # reset list
            ls = []
            break
        else:
            search = ms.searchKeyword(ls[keyword])
            print(search)


def searchActors(ms):
    ls = actors
    ls.append("Go Back")
    while True:
        actor = TerminalMenu(
            ls, title="\nWhat actor would like to search for?").show()
        # "go back" option is last option
        if actor == len(ls) - 1:
            # reset list
            ls = []
            break
        else:
            search = ms.searchActors(ls[actor])
            print(search)


def main():
    # create a new movie script object
    ms = MovieScript(seq, actors, sceneTimings)
    print("\n~~~~~ Welcome to the spy movie app! ~~~~~~")
    while True:

        entry_point = TerminalMenu(
            ["View Script", "View Call Sheet", "View Scene Timings", "Search Keyword(s)", "Search Actors", "Shuffle Script", "Exit"], title="\nWhat would you like to do?").show()

        if entry_point == 0:
            # calling __str__ method on MovieScript class
            print("\n")
            print(ms)
        elif entry_point == 1:
            print("\n")
            print(ms.printCallSheet())
        elif entry_point == 2:
            print("\n")
            print(ms.printSceneTimings())
        elif entry_point == 3:
            print("\n")
            searchKeywords(ms)
        elif entry_point == 4:
            print("\n")
            searchActors(ms)
        elif entry_point == 5:
            print("\n")
            shuffledScript = seq
            random.shuffle(shuffledScript)
            ms = MovieScript(shuffledScript, actors, sceneTimings)
            print(ms)
        else:
            print("\n")
            print("Goodbye!")
            exit()


if __name__ == "__main__":
    main()
