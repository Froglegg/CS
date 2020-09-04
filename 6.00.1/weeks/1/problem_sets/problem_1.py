# Write a program that counts up the number of vowels contained in the string s
s = "hey mac donald"
count = 0
for i in s.lower():
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1
print("Number of vowels: " + str(count))
