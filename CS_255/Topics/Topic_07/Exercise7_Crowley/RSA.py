from RSA_Prime import RSA_Prime
from Modular_Exponentiation import modular_Exponentiation, modInverse


class RSA:
    '''
    RSA class for practicing RSA encryption / decryption using integer messages ONLY
    Further configuration required for alphanumeric text, other data types, etc.
    '''
    # RSA class inits with optional p,q,e inputs, else it will calculate a strong (by modern standards) p, q, and e

    def __init__(self, p=None, q=None, e=None, d=None) -> None:
        self._p, self._q = (p, q) if p and q else self._generatePrimes()
        self._n = self._generate_RSA_modulus(self._p, self._q)
        self._e = e if e else self._generate_encryption_exponent()
        self._d = d if d else self._calculate_decryption_exponent(
            self._p, self._q, self._e)

    def _generatePrimes(self) -> tuple:
        ''' 
        NOTE: This isn't used in exercise 7
        Returns a tuple of two large random primes based on bit length n
        For RSA, the RSA modulus n should be between 2048 to 4096 bits
        Thus, each prime should be between 1024 to 2048 bits in length
        '''
        return(RSA_Prime(1024), RSA_Prime(1024))

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
        # d = modular_Exponentiation(e, -1, φ_n)
        d = modInverse(e, φ_n)

        return d

    def getPublicKeyPair(self) -> tuple:
        return (self._n, self._e)

    def encryptMessage(self, m) -> int:
        n, e = self.getPublicKeyPair()

        c = modular_Exponentiation(m, e, n)

        return c

    def decryptMessage(self, c: int):
        message_int = modular_Exponentiation(c, self._d, self._n)

        return message_int
