string = "this is a phrase"
str1 = string.split("\n")
print(str1)
result1 = [line.strip().split() for line in string.split('\n')]
print(result1)
string = "this is another phrase"
result2 = [line.strip().split() for line in string.split('\n')]

result = [result1, result2]
print(result)

[[['this', 'is', 'a', 'phrase']], [['this', 'is', 'another', 'phrase']]]
