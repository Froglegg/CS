from simple_term_menu import TerminalMenu
from Collections.LinkedDirectedGraph import LinkedDirectedGraph

airports = ["ATL", "NYC", "LA", "SF", "SEA", "CHI", "MIA", "DEN"]


def buildRoute(g: LinkedDirectedGraph):

    fromVertex = airports[TerminalMenu(
        airports, title="\nBuild route from...").show()]
    toVertex = airports[TerminalMenu(
        airports, title="\nBuild route to...").show()]
    distance = int(
        input(f"\nWhat is the distance from {fromVertex} to {toVertex}? Integers only: "))
    edge = g.addEdge(fromVertex, toVertex, distance)
    print(f"\nRoute added: {edge}")


def findShortestPaths(g: LinkedDirectedGraph):
    fromVertex = airports[TerminalMenu(
        airports, title="\nFind the shortest route from...").show()]

    return g.shortestPaths(g.getVertex(fromVertex))


def main():

    routeGraph = LinkedDirectedGraph(airports, edgeLabel="Flight miles")

    print("\nWelcome to the flight scheduler, a CLI for building graphs of flight routes and their shortest paths.\n")

    while True:
        entry = TerminalMenu(["View Flight Graph", "Build Routes",
                              "Find Shortest Paths", "Exit"], title="\nWhat would you like to do?").show()

        if entry == 0:
            routeGraph.printGraph()

        elif entry == 1:
            buildRoute(routeGraph)

        elif entry == 2:
            shortestPaths = findShortestPaths(routeGraph)
            print(shortestPaths["title"])
            print(shortestPaths["table"])

        else:
            print("Goodbye!")
            exit()


if __name__ == "__main__":
    main()
