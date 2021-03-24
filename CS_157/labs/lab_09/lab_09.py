# Richard Hayes Crowley
# 03/17/2020
# CSC_157
def decodeFile():
    fr = open("sentences.txt")
    codeKey = [[0, 1, 2, 4, 7, 14], [6, 7], [1, 16], [5, 7, 8], [14, 18]]
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
    return "".join(steganograph)


secret_message = decodeFile()
print('Richard Hayes Crowley\nCSC_157\n\n')
print(f'The secret message is: {secret_message}')

line = "the enemy has advanced"
listLine = [ch for ch in line]
for x in range(0, len(listLine)):
    if (x % 4 == 0):
        print(listLine[x], end="")
print("\n\n")
