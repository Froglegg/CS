def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """

    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
    score_card = []
    word = word.lower()
    for idx, l in enumerate(word):
        score_card.append((alphabet_list.index(l) + 1)*idx)
    biggest = max(score_card)
    score_card.remove(biggest)
    second_biggest = max(score_card)
    return f(biggest, second_biggest)


score("eee", lambda x, y: print(x, y))
