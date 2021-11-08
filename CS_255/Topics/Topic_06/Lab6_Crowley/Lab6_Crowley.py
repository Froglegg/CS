# Richard Hayes Crowley
# CSC_255_Ex_06
from os import listdir
from HuffmanClass import HuffmanClass
import base64


def main():
    inputList = []

    for file in listdir("./Input-Output-Files"):
        # find all files in current directory that end in .txt

        if file.endswith("in.txt"):

            outputFileName = file.split("in.txt")[0]

            # open file in binary mode and read to lines ref
            lines = open(f'./Input-Output-Files/{file}', 'rb').read()

            # prepare encoded string for variable encoding based on file type
            # prepare b64 boolean to tell the program which encoding the input is in
            encodedString = lines
            b64Boolean = False

            # try to read in file as ascii, for example, regular text files
            # if ascii works, then we can use the regular binary byte stream
            try:
                lines.decode('ascii')

            # if it throws a UnicodeDecodeError, as happens with PDFs, encode lines into bytes using base 64
            except UnicodeDecodeError:
                encodedString = base64.b64encode(lines)
                b64Boolean = True

            # append fileName encodedString, and b64Boolean to input list
            inputList.append((outputFileName, encodedString, b64Boolean))

    # for each input in input list, write output file
    for input in inputList:
        # fileName is first item in input tuple
        filePrefix = input[0]
        # b64 boolean is last item in input tuple
        b64Boolean = input[-1]

        inputFileName = filePrefix + "in.txt"
        encodedFileName = filePrefix + "encoded.txt"
        debugFileName = filePrefix + "debug.txt"
        decodedFileName = filePrefix + "decoded.txt"

        print(
            f"*** Testing file {inputFileName}, debug output file {debugFileName} ***")

        # Instantiate HuffmanClass, HuffmanClass encodes input using Huffman's Algorithm upon initialization
        HuffmanTree = HuffmanClass(input[1])

        freqTable = HuffmanTree.getFrequencyTable()

        priorityQueue = HuffmanTree.getPriorityQueue()

        encodingTable = HuffmanTree.getEncodingTable()

        encodedString = HuffmanTree.getEncoding()

        # run Huffman decoding algorithm
        decodedString = HuffmanTree.HuffmanDecode(encodedString)

        # if input type was b64, for example, for PDFs, convert decoded string to base64
        if b64Boolean:
            decodedString = base64.b64decode(
                HuffmanTree.HuffmanDecode(encodedString))

        with open(f"./Input-Output-Files/{encodedFileName}", 'w') as f:
            f.write(encodedString)
            f.close()

        with open(f"./Input-Output-Files/{decodedFileName}", 'wb') as f:
            f.write(decodedString)
            f.close()

        with open(f"./Input-Output-Files/{debugFileName}", 'w') as f:
            '''
            Debugging step requires a lot of sorting and decoding bytes into strings to fit the debug file output format.
            Nothing here affects the Huffman algorithm itself, only the output of this driver program
            '''

            f.write(f"Encoding {inputFileName} -> {encodedFileName}\n")

            # create new list and append items from frequency table and sort by ASCII value of character (ord(x[0]))
            f.write(f"\ncountCharacters:\n\n")

            freqList = sorted(freqTable.items(), key=lambda x: x[0])

            for item in freqList:
                f.write(f" {ord(item[0].decode())} {ascii(item[0].decode())} " +
                        "{" + str(item[1]) + "}\n")

            # create new list and append items from priority queue and sort by Frequency ascending, and then by ASCII value of character (ord(x)[0])
            f.write("\nprintQueue:\n\n")

            pqList = sorted([(ord(item._value.value.decode()), ascii(item._value.value.decode()),
                              item._key) for item in priorityQueue], key=lambda x: (x[2], x[0]))

            for item in pqList:
                f.write(f" {item[0]} {item[1]} " +
                        "{" + str(item[2]) + "}\n")

            # create new list and append items from encoding table and sort by ASCII value of character (ord(x[0]))
            f.write("\nmakeBitData:\n\n")

            encodingList = sorted([(ord(item[0].decode()), ascii(item[0].decode()), item[1])
                                   for item in encodingTable.items()], key=lambda x: (x[0]))

            for item in encodingList:
                f.write(f" {item[0]} {item[1]} " +
                        "{" + str(item[2]) + "}\n")

            # Decoding has already taken place (see decodedString above)
            # here, we are simply diff/compare the two files
            f.write(f"\nDecoding {encodedFileName} -> {decodedFileName}\n")
            inputFile = open(f'./Input-Output-Files/{inputFileName}', 'rb',)
            decodedFile = open(
                f'./Input-Output-Files/{decodedFileName}', 'rb',)

            if inputFile.read() == decodedFile.read():
                f.write(
                    f"\n!!! Files {inputFileName} and {decodedFileName} are equal.\n")
                print("\nOK\n\n")

            else:
                f.write(
                    f"\n!!! Files {inputFileName} and {decodedFileName} are NOT equal.\n")

            inputFile.close()
            decodedFile.close()
            f.close()


if __name__ == "__main__":
    main()
