n = 0
while n < 5:
    print(n)
    n += 1
for var in range(5):
    print(var)

for var in range(1, 10, 2):
    print(var)

mysum = 0
for i in range(5):
    mysum += 1
    print(mysum)
    if mysum == 3:
        print('break')
        break
print(mysum)

print("Hello!")
foo = 10
while foo > 0:
    print(foo)
    foo -= 2

for i in range(2, 12, 2):
    print(i)
print('Goodbye!')

print("Hello")
for i in range(10, 0, -2):
    print(i)

result = 0
for i in range(6):
    result += (i + 1)
print(result)

num = 10
for num in range(5):
    print(num)
print(num)

print(0/2)

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')

print(0 % 4)

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))
