def isPalindrome(s):
    """

    """
    def toChar(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(toChar(s[1:-1]))

    return isPal(toChar(s))


print(isPalindrome("Able was I, ere I saw elba"))