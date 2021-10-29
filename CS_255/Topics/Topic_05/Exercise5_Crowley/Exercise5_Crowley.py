# Richard Hayes Crowley
# CSC_255_Exercise_05
from os import listdir
from Graph import Graph
from Kruskal import Kruskal


def main():
    inputList = []

    for file in listdir("."):
        # find all files in current directory that end in .txt

        if file.startswith("in") and file.endswith(".txt"):

            outputFileName = "out" + file.split("in")[1]

            # break into list of lines
            lines = open(file, 'r').readlines()
            # remove first line that contains instructions
            lines.pop(0)

            # # list comprehension to get our lines of integers into the proper format
            joinedInputList = [[int(item) for item in "".join(sublist).split(' ') if item != ""] for sublist
                               in "".join(lines).split("\n") if len(sublist) > 0]

            inputList.append((outputFileName, joinedInputList))

    # for each result in result list, write output file
    for input in inputList:
        # fileName is first item in input tuple
        fileName = input[0]

        inputGraph = Graph()

        # for each edge in inputlist, insert corresponding vertices and edge to graph
        for sublist in input[1]:
            vertexA = inputGraph.insert_vertex(sublist[0])
            veretexB = inputGraph.insert_vertex(sublist[1])
            edge = inputGraph.insert_edge(vertexA, veretexB, sublist[2])

        edge: Graph.Edge
        edgeList = []

        # iterate through edges in graph, append edge properties to edgeList
        for edge in inputGraph.edges():
            origin, destination = edge.endpoints()
            weight = edge.weight()
            edgeList.append((int(origin), int(destination), int(weight)))

        # sort edgeList by origin, which is the first item in the edge tuple, and then by destination,
        # and then finally by weight, to match format of output files
        edgeList.sort(key=lambda edge: (edge[0], edge[1], edge[2]))

        MST = Kruskal(inputGraph)

        mstEdgeList = []
        mstTotalWeight = 0

        for edge in MST:
            origin, destination = edge.endpoints()
            weight = edge.weight()
            mstEdgeList.append((int(origin), int(destination), int(weight)))
            mstTotalWeight += weight

        # sort mstEdgeList by edge weight, which is the last item in the edge tuple
        mstEdgeList.sort(key=lambda edge: (edge[2], edge[0], edge[1]))

        with open(f"{fileName}", 'w') as f:
            f.write(f'Graph edges: vertice1, vertice2, weight of the edge\n\n')
            for edge in edgeList:
                f.write(f"edge: {edge[0]}, {edge[1]}, {edge[2]}\n")
            f.write("\n")
            f.write(
                f'Kruskal spanning tree edges: vertice1, vertice2, weight of the edge\n\n')
            for edge in mstEdgeList:
                f.write(f"edge: {edge[0]}, {edge[1]}, {edge[2]}\n")
            f.write("\n")
            f.write(f'Kruskal spanning tree weight is {mstTotalWeight}\n')


if __name__ == "__main__":
    main()
