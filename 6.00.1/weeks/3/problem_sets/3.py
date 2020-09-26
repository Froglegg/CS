def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in lettersGuessed:
        alphabet.remove(letter)
    return "".join(alphabet)


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
# abcdfghjlmnoqtuvwxyz
