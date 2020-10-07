data = []
file_name = input("please enter a file name: ")

try:
    fh = open(file_name, 'r')
except IOError:
    print("cannot open " + file_name)
else:
    for new in fh:
        if new != "\n":
            addIt = new[:-1].split(",")
            data.append(addIt)
finally:
    print(data)
    fh.close()
