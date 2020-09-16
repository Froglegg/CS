# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# s = 'dqbyeewyeozoi'
# expected eewy
# s = 'azcbobobegghakl'
# expected beggh

s = "unlzbqjiyqtuwszwoctx"
# expected qtuw
longestAlphabeticSubString = ""
string = ""
for idx, char in enumerate(s):
    if char >= s[idx - 1] or string == char:
        string += char
        if len(string) > len(longestAlphabeticSubString):
            longestAlphabeticSubString = string
    else:
        string = char
print("Longest substring in alphabetical order is: " + longestAlphabeticSubString)

for char in s:
    print(s.index(char))

for idx, char in enumerate(s):
    print(s[idx])
