# Write a program that prints the number of times the string 'bob' occurs in s.
s = str('heybobobheybob')

i = 0
count = 0

while i < len(s):
    s = s[i:len(s)]
    try:
        i = s.index("bob") + 1
        count += 1
    except:
        print("Number of times bob occurs is: " + str(count))
        break


# def iterate(string, i=0, count=0):
#     count = count
#     string = string[i:len(string)]
#     try:
#         if string.index("bob"):
#             i = string.index("bob") + 1
#             count += 1
#             iterate(string, i, count)
#     except:
#         print("Number of times bob occurs is: " + str(count))

# iterate(s)
