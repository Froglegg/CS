def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    arr = []
    for char in secretWord:
        if char not in lettersGuessed:
            arr.append("_")
        else:
            arr.append(char)
    return "".join(arr)


secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
lettersGuessed2 = ['a', 'p', 'p', 'l', 'e', 'g', 'e', 'p']
print(getGuessedWord(secretWord, lettersGuessed))
