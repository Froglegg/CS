# Richard Hayes Crowley
# CSC_255_Ex_06
from os import listdir
from HuffmanClass import HuffmanClass


def main():
    inputList = []

    for file in listdir("."):
        # find all files in current directory that end in .txt

        if file.endswith("in.txt"):

            outputFileName = file.split("in.txt")[0]

            # break into list of lines
            lines = open(file, 'rb').readlines()

            # join lines into input string
            joinedLines = b"".join(lines)

            # append fileName and joinedLines to input list
            inputList.append((outputFileName, joinedLines))

    # for each input in input list, write output file
    for input in inputList:
        # fileName is first item in input tuple
        filePrefix = input[0]

        inputFileName = filePrefix + "in.txt"
        encodedFileName = filePrefix + "encoded.txt"
        debugFileName = filePrefix + "debug.txt"
        decodedFileName = filePrefix + "decoded.txt"

        encoded = HuffmanClass(input[1])

        encoded.encoded.printTree()

        # freqTable = encoded.getFrequencyTable()

        # priorityQueue = encoded.getPriorityQueue()

        # encodingTable = encoded.getEncodingTable()

        # encodedString = encoded.getEncoding()

        # decodedString = encoded.decode(encodedString)

        # encoded.printTree()

        # with open(f"{encodedFileName}", 'w') as f:
        #     f.write(encodedString)
        #     f.close()

        # with open(f"{decodedFileName}", 'w') as f:
        #     f.write(decodedString)
        #     f.close()

        # with open(f"{debugFileName}", 'w') as f:
        #     '''
        #     Debugging step requires a lot of sorting and re-arranging to fit the debug file output format.
        #     Nothing here affects the Huffman algorithm itself, only how its output is printed
        #     '''

        #     f.write(f"Encoding {inputFileName} -> {encodedFileName}\n")

        #     # create new list and append items from frequency table and sort by ASCII value of character (ord(x[0]))
        #     f.write(f"\ncountCharacters:\n\n")

        #     freqList = sorted(freqTable.items(), key=lambda x: ord(x[0]))
        #     for item in freqList:
        #         f.write(f" {ord(item[0])} {repr(item[0])} " +
        #                 "{" + str(item[1]) + "}\n")

        #     # create new list and append items from priority queue and sort by Frequency ascending, and then by ASCII value of character (ord(x)[0])
        #     f.write("\nprintQueue:\n\n")

        #     pqList = sorted([(ord(item._value.value), repr(item._value.value),
        #                       item._key) for item in priorityQueue], key=lambda x: (x[2], x[0]))

        #     for item in pqList:
        #         f.write(f" {item[0]} {item[1]} " +
        #                 "{" + str(item[2]) + "}\n")

        #     # create new list and append items from encoding table and sort by ASCII value of character (ord(x[0]))
        #     f.write("\nmakeBitData:\n\n")

        #     encodingList = sorted([(ord(item[0]), repr(item[0]), item[1])
        #                            for item in encodingTable.items()], key=lambda x: (x[0]))

        #     for item in encodingList:
        #         f.write(f" {item[0]} {item[1]} " +
        #                 "{" + str(item[2]) + "}\n")

        #     # Decoding has already taken place (see decodedString above)
        #     # here, we are simply diff/compare the two files
        #     f.write(f"\nDecoding 5_encoded.txt -> 5_decoded.txt\n")
        #     inputFile = open(inputFileName, 'rb')
        #     inputFileLines = inputFile.readlines()
        #     decodedFile = open(decodedFileName, 'rb')
        #     decodedFileLines = decodedFile.readlines()
        #     if inputFileLines == decodedFileLines:
        #         f.write(
        #             f"\n!!! Files {inputFileName} and {decodedFileName} are equal.\n")
        #     else:
        #         f.write(
        #             f"\n!!! Files {inputFileName} and {decodedFileName} are NOT equal.\n")

        #     inputFile.close()
        #     decodedFile.close()
        #     f.close()


if __name__ == "__main__":
    main()
