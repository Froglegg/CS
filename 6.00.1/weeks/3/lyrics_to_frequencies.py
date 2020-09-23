def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1

    return myDict


def string_to_list(string):
    return string.split(" ")


beatles = string_to_list(
    "Sie liebt dich yeah yeah yeah Sie liebt dich yeah yeah yeah Sie liebt dich yeah yeah yeah yeah")

freq_dict = lyrics_to_frequencies(beatles)


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


# (w, b) = most_common_words(freq_dict)
# tup = most_common_words(freq_dict)
# print(w, b)
# print(tup)

# finds the words that occur at least a certain number of
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        print(temp[1])
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result


print(words_often(freq_dict, 5))
