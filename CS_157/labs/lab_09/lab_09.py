# word count function
def wordCount():
    fr = open("sentences.txt")
    line = fr.readline()
    while (line):
        line = line.lower()
        line = line.split(" ")
        print("word count: ", len(line))
        line = fr.readline()
    fr.close()


def vowelCount():
    fr = open("sentences.txt")
    line = fr.readline()
    while (line):
        line = line.lower()
        print("vowel count: ",
              len([v for v in line if v in "aeiou"]))
        line = fr.readline()
    fr.close()


def decodeFile():
    fr = open("sentences.txt")
    codeKey = [[0, 1, 2, 4, 7, 14], [6, 7], [1, 16, 19], [7, 8], [14, 18]]
    line = fr.readline()
    steganograph = []
    while_loop_idx = 0
    while(line):
        for idx, value in enumerate(line):
            for code in codeKey[while_loop_idx]:
                if (idx == code):
                    steganograph.append(value)
        while_loop_idx += 1
        line = fr.readline()
    print(steganograph)
    return steganograph


decodeFile()
# wordCount()

# print("")

# vowelCount()

# print("")
