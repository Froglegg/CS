
import os
for root, dirs, files in os.walk("/Users/frogLegg/Desktop/CS/CS_157/labs"):
    for file in files:
        if file.endswith(".rtf"):
            # print(file)
            fileString = str(file).replace(".rtf", "_QA.rtf")
            print(fileString)
            # os.system("mv ${file} ${fileString}")
            # print(os.path.join(root, file))
            # os.system('mv')
