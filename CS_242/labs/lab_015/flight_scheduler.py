import db.directed_graph_db as db
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

    global conn
    # create a database connection
    conn = db.createConnection("./db/graphs.db")

    # create table
    if conn is not None:
        # create contacts table
        db.createTable(conn)
    else:
        print("Error! cannot create the database connection.")

    with conn:
        def readTable():
            return db.readTable(conn)

        def saveGraph(graphLabel, graphData):
            try:
                db.insertIntoTable(conn, [graphLabel, graphData])
            except:
                print("Something went wrong trying to save your graph to the database!")

        def updateGraph(graphLabel, graphData, graphId):
            try:
                db.updateTable(conn, [graphLabel, graphData, graphId])
            except:
                print(
                    "Something went wrong trying to update your graph in the database!")

        def deleteGraph(graphId):
            try:

                db.deleteFromTable(conn, graphId)

            except:
                print(
                    "Something went wrong trying to delete your graph from the database!")

        def viewGraph(id, name, routeGraph):
            print(f"\nViewing {name}")
            while True:
                entry = TerminalMenu(["View Flight Graph", "Build Routes",
                                      "Find Shortest Paths", "Save Graph", "Exit"], title=f"\nWhat would you like to do with {name}?").show()

                if entry == 0:
                    routeGraph.printGraph()

                elif entry == 1:
                    buildRoute(routeGraph)

                elif entry == 2:
                    shortestPaths = findShortestPaths(routeGraph)
                    print("\n")
                    print(shortestPaths["title"])
                    print(shortestPaths["table"])
                elif entry == 3:

                    graphJson = routeGraph.saveJson()
                    updateGraph(name, graphJson, id)

                else:
                    break

        print("\nWelcome to the flight scheduler, a CLI for building graphs of flight routes and their shortest paths.\n")

        currentGraph = LinkedDirectedGraph()

        while True:
            entry = TerminalMenu(["Build new flight graph", "Load flight graph", "Delete flight graph",
                                  "Exit"], title="\nWhat would you like to do?").show()
            if entry == 0:

                name = input("Please enter a name for your graph: ")

                newRouteGraph = LinkedDirectedGraph(
                    airports, edgeLabel="Flight miles")

                graphJson = newRouteGraph.saveJson()

                saveGraph(name, graphJson)

            elif entry == 1:
                table = readTable()

                graphList = [i[1] for i in table]

                selection = TerminalMenu(
                    graphList, title="\nWhich graph would you like to view?").show()

                for i in table:
                    if i[1] == graphList[selection]:
                        currentGraph.loadJson(i[2])

                        viewGraph(id=i[0], name=i[1], routeGraph=currentGraph)

            elif entry == 2:
                table = readTable()
                graphList = [i[1] for i in table]
                selection = TerminalMenu(
                    graphList, title="\nWhich graph would you like to delete?").show()
                for i in table:
                    if i[1] == graphList[selection]:

                        deleteGraph(i[0])

            else:
                print("goodbye!")
                exit()


if __name__ == '__main__':
    main()
