import array as arr
msg = ["H", "e", "l", "l", "o", "S", "t", "u", "d", "e", "n", "t"]
str1 = []
str2 = []

print("Rail Fence - Encryption\n\n")
print("Plain Text: HelloStudent\n\n")

for i in range(len(msg)):
    if (i % 2 == 0):

        str1.append(msg[i])

    else:
        str2.append(msg[i])

print("Cipher Text:", "".join(str1 + str2))
# output
# Rail Fence - Encryption


# Plain Text: HelloStudent


# Cipher Text: HlotdnelSuet
