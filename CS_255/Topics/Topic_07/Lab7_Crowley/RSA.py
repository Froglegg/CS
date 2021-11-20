from RSA_Prime import RSA_Prime
from Modular_Exponentiation import modular_Exponentiation, modInverse
from string import ascii_lowercase


class RSA:
    '''
    RSA class for practicing RSA encryption / decryption using integer messages ONLY
    Further configuration required for alphanumeric text, other data types, etc.
    '''

    # helper functions
    def build_alphabet_cipher(self) -> dict:
        ''' 
        Maps letters of the alphabet to strings where a = "01" and z = "26"
        Returns alphabet cipher <dict>
        '''

        lowercase_alphabet = ascii_lowercase

        alphabet_cipher = {}

        for idx, l in enumerate(lowercase_alphabet):
            alphabet_cipher[l] = f"{idx+1:02}"
            alphabet_cipher[f"{idx+1:02}"] = l

        return alphabet_cipher

    def convert_word_to_int(self, word: str) -> int:
        '''
        Converts alphabetic string to integer by iterating over characters and looking up their integer values from the alphabet cipher
        Returns integer representation of string
        '''
        int_string = ""
        for c in word:
            int_string += self._alphabet_cipher[c.lower()]
        return int(int_string.ljust(6, "0"))

    def __init__(self, p=None, q=None, e=None, d=None) -> None:
        '''
        RSA class inits with optional p,q,e inputs, else it will calculate a strong (by modern standards) p, q, and e
        This RSA class is compatible with integers and lowercase letters of the alphabet
        '''
        self._alphabet_cipher = self.build_alphabet_cipher()
        self._p, self._q = (p, q) if p and q else self._generatePrimes()
        self._n = self._generate_RSA_modulus(self._p, self._q)
        self._e = e if e else self._generate_encryption_exponent()
        self._d = d if d else self._calculate_decryption_exponent(
            self._p, self._q, self._e)

    def _generatePrimes(self) -> tuple:
        ''' 
        NOTE: This isn't used in exercise or lab 7
        Returns a tuple of two large random primes based on bit length n
        For RSA, the RSA modulus n should be between 2048 to 4096 bits
        Thus, each prime should be between 1024 to 2048 bits in length
        '''
        return(RSA_Prime(1024), RSA_Prime(1024))

    def _generate_RSA_modulus(self, p, q) -> int:
        '''
        generate n, the RSA modulus
        '''
        return p * q

    def _generate_encryption_exponent(self) -> int:
        '''
        Select prime encryption exponent e so that 3 ≤ e ≤ n−1 and gcd(e,(p-1)(q-1)) = 1.
        NOTE: most common encryption and signing number for RSA is the Fermat number 65537. 
        This isn't used in Exercise 7 or Lab 7.
        '''
        return 65537

    def _calculate_decryption_exponent(self, p, q, e) -> int:
        '''
        Compute decryption exponent which is the modular inverse of e, 
        so e⋅d modφ(n) = 1. The inverse is calculated as d = λ modφ(n), 
        where λ is a result of extended Euclidean algorithm equation 
        e⋅λ+φ(n)⋅μ = gcd(e,φ(n))
        '''

        # calculate Euler totient φ
        φ_n = (p-1)*(q-1)

        # find modular inverse of the encryption exponent using the totient
        # this is our decryption exponent
        # d = modular_Exponentiation(e, -1, φ_n)
        d = modInverse(e, φ_n)

        return d

    def getPublicKeyPair(self) -> tuple:
        '''
        Returns (n,e)
        '''
        return (self._n, self._e)

    def encryptMessage(self, m) -> int:
        ''''
        Performs encryption on message
        If message is a string, perform string to int conversion
        Returns encrypted message c <int>
        '''
        n, e = self.getPublicKeyPair()

        if type(m) is str:
            m = self.convert_word_to_int(m)

        c = modular_Exponentiation(m, e, n)

        return c

    def decryptMessage(self, c: int, alphabetic=True):
        '''
        Decrypts message
        If original message was an integer and wasn't converted to an integer based on the alphabet cipher, 
        skip conversion step
        Returns (decrypted_message_int, decrypted_message_str)
        '''
        message_int = modular_Exponentiation(c, self._d, self._n)
        message_str = ""

        # conversion step
        if alphabetic:
            message_int_str = "0"+str(message_int)

            # step through message for every two  digits
            for i in range(0, len(message_int_str), 2):
                subStr = message_int_str[i:i+2]
                message_str += self._alphabet_cipher[subStr]

        return (message_int, message_str)
