
# import os
# import subprocess
# for root, dirs, files in os.walk("/Users/frogLegg/Desktop/CS/CS_157/labs"):
#     for file in files:
# if file.endswith(".rtf"):
#     print(file)
#     fileString = str(file).replace(".rtf", "_QA.rtf")

#             subprocess.run("mv ${file} ${fileString}")
#             # print(fileString)
#             # os.system("mv ${file} ${fileString}")
#             # print(os.path.join(root, file))
#             # os.system('mv')

import os
import shutil

for root, subdirs, files in os.walk("."):
    for f in files:
        if f.endswith(".rtf"):
            fileString = str(f).replace(".rtf", "_QA.rtf")
            print(f)
            print(fileString)
            shutil.copy(os.path.join(root, f), os.path.join(root, fileString))
            # os.(os.path.join(root, f), os.path.join(root, fileString))
