# from Crypto.Util import number
from string import ascii_lowercase
from Modular_Exponentiation import modular_Exponentiation, modInverse
from RSA_Prime import RSA_Prime


class RSA:

    # helper functions
    def build_alphabet_cipher(self) -> dict:

        lowercase_alphabet = ascii_lowercase

        alphabet_cipher = {}

        for idx, l in enumerate(lowercase_alphabet):
            alphabet_cipher[l] = f"{idx+1:02}"
            alphabet_cipher[f"{idx+1:02}"] = l

        return alphabet_cipher

    def convert_word_to_int(self, word: str) -> int:
        int_string = ""
        for c in word:
            int_string += self._alphabet_cipher[c.lower()]
        return int(int_string.ljust(6, "0"))

    def extended_Euclidean_Algorithm(self, a, b):
        # Base Case
        if a == 0:
            return b, 0, 1

        gcd, x1, y1 = self.extended_Euclidean_Algorithm(b % a, a)

        # Update x and y using results from recursive call
        x = y1 - (b//a) * x1
        y = x1

        return gcd, x, y

    def smallPrimesList(n):
        ''' 
        primes function builds a list of primes up to a number n, exclusive
        we use this function in double hashing to find the greatest prime that is less than the total length of the table
        '''
        # simple sieve of multiples
        odds = range(3, n, 2)
        sieve = set(sum([list(range(q*q, n+1, q+q))
                         for q in odds], []))
        return [2] + [p for p in odds if p not in sieve]

    # RSA class inits with optional p,q,e inputs, else it will calculate a strong (by modern standards) p, q, and e
    def __init__(self, p=None, q=None, e=None, d=None) -> None:
        self._alphabet_cipher = self.build_alphabet_cipher()
        self._p, self._q = (p, q) if p and q else self._generatePrimes()
        self._n = self._generate_RSA_modulus(self._p, self._q)
        self._e = e if e else self._generate_encryption_exponent()
        self._d = d if d else self._calculate_decryption_exponent(
            self._p, self._q, self._e)

    def _generatePrimes(self) -> tuple:
        ''' 
        Pycrypto is an open-source package with common functions used in cryptography
        Here, we are using its getPrime() function, which returns a large random prime based on bit length
        For RSA, the RSA modulus n should be between 2048 to 4096 bits
        Thus, each prime should be between 1024 to 2048 bits in length
        '''
        return(RSA_Prime(), RSA_Prime())

    def _generate_RSA_modulus(self, p, q) -> int:
        return p * q

    def _generate_encryption_exponent(self) -> int:
        '''
        Select prime encryption exponent e so that 3 ≤ e ≤ n−1 and gcd(e,(p-1)(q-1)) = 1.
        NOTE: most common encryption and signing number for RSA is the Fermat number 65537
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
        d = modular_Exponentiation(e, -1, φ_n)
        # d = modInverse(e, φ_n)

        return d

    def getPublicKeyPair(self) -> tuple:
        return (self._n, self._e)

    def encryptMessage(self, m) -> int:
        n, e = self.getPublicKeyPair()

        # if type(m) is str:
        #     message_int = self.convert_word_to_int(m)

        c = modular_Exponentiation(m, e, n)

        return c

    def decryptMessage(self, c: int):
        message_int = modular_Exponentiation(c, self._d, self._n)
        # message_int_str = "0"+str(message_int)

        # decrypted_message = ""
        # step through message for every two  digits
        # for i in range(0, len(message_int_str), 2):
        #     subStr = message_int_str[i:i+2]
        #     decrypted_message += self._alphabet_cipher[subStr]

        return message_int

# from introduction to cryptograohy pdf
# test = RSA(885320963, 238855417, 9007)

# from Murashkina's assignment PDF
# p 7
# q 37
# e 257
# d 137
# M 65(just one letter ‘A’)


# test = RSA(p, q, e, d)
# # publicKeyPair = test.getPublicKeyPair()
# encryptedMessage = test.encryptMessage(65)

# decryptedMessage = test.decryptMessage(151)
# print(decryptedMessage)

# FOR EXERCISE!!
# studentName Student7
# Given to student p,q,e,r
# r is encrypted message, s is decrypted message
# goal is to find n, d, s

p = 13
q = 149
e = 257
r = 1907

test = RSA(p, q, e)


s = test.decryptMessage(r)
n = test.getPublicKeyPair()[0]

print(f"RSA Modulus n: {n}")
print(f"Decryption exponent d: {test._d}")
print(f"Decrypted message s: {s}")
