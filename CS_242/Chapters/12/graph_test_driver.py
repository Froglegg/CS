from LinkedDirectedGraph import LinkedDirectedGraph

g = LinkedDirectedGraph(["A", "B", "C", "D", "E"])

edgeList = [["C", "A", 3], ["A", "C", 4], ["B", "C", 2],
            ["A", "B", 5], ["C", "B", 8], ["C", "D", 4]]

for edge in edgeList:
    g.addEdge(edge[0], edge[1], edge[2])

g.printGraph()

# shortestPath = g.shortestPaths(test)
# print('hey')
# print(shortestPath["title"])
# print(shortestPath["table"])
