# Richard Hayes Crowley
# CSC_255_Lab_04
from os import listdir

from Heaps.AdaptableHeapPriorityQueue import AdaptableHeapPriorityQueue as Heap


def main():
    inputList = []

    for file in listdir("."):
        # find all files in current directory that end in .txt

        if file.startswith("in") and file.endswith(".txt"):

            outputFileName = "out" + file.split("in")[1]

            # break into list of lines
            lines = [line for line in open(file, 'r')]

            # # join list of lines into string and then split on blank \n spaces
            joinedList = [int(i) for i in "".join(lines).split()]

            # # # append outputFileName and joinedList as a tuple
            inputList.append((outputFileName, joinedList))

    # for each result in result list, write output file
    for input in inputList:

        heap = Heap()
        fileName = input[0]
        for i in input[1]:
            heap.add(i, i)

        print(heap[0])

        with open(f"{fileName}", 'w') as f:
            f.write(f'Heap\n{heap.getData()}\n\n')
            f.write(f'Insert 31\n')
            # insert key value tuple
            heap.add(31, 31)
            f.write(f'Heap after insert 31\n{heap.getData()}\n\n')
            f.write(f'Insert 14\n')
            # insert key value tuple
            heap.add(14, 14)
            f.write(f'Heap after insert 14\n{heap.getData()}\n\n')
            while not heap.is_empty():
                f.write("Delete min\n")
                heap.remove_min()
                f.write(f"Heap after Delete min\n{heap.getData()}\n\n")
            f.write(f'Deleted all\n')


if __name__ == "__main__":
    main()
