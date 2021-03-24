# RICHARD HAYES CROWLEY
# CSC_157_LAB_11

import pickle
import re


booyah_txt = open("booyah.txt", "r").read()
tel_txt = open("telephone.txt", "r").read()

words_file = "words.pickle"
tel_file = "tel.pickle"

# open the files for writing
wordsObject = open(words_file, "wb")
telObject = open(tel_file, "wb")

# pickle dump
pickle.dump(booyah_txt, wordsObject)
pickle.dump(tel_txt, telObject)
# here we close the fileObjects
wordsObject.close()
telObject.close()

# we open the files for reading
wordsObject = open(words_file, "rb")
telObject = open(tel_file, "rb")
# load the objects from the file into test strings
words_string = pickle.load(wordsObject)
tel_string = pickle.load(telObject)

search_word = "Booyah"

wordsCt = len(re.findall(r"[\w']+", words_string))
print("Total Word Count = ", wordsCt)
# Ignore case regex
wordsBC = len(re.findall(search_word, words_string, flags=re.IGNORECASE))
print("Total Booyah Count = ", wordsBC)
wordsDiff = (len(re.findall(r"[\w']+", words_string)) - wordsBC)
print("Total w / o Booyah = ", wordsDiff)
wordsObject.close()

# remove anything other than digits from tel_string
number = re.sub(r"\D", "", tel_string)
print("Telephone Number : ", number)

telObject.close()

msg = "dept 32, code 300; type 43"
pattern = "\d+"
result = re.findall(pattern, msg)
print(result)

msg = "tunnel entrance"
chkMatch = re.search("\Atunnel", msg)

if (chkMatch):
    print("a pattern was found inside the string")
else:
    print("a pattern was not found")
