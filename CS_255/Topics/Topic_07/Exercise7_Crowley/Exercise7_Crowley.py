from RSA import RSA


def main():
    # input as found in Exercise7_in7_to_student_Crowley.txt
    # first prime p

    p = 13
    # second prime q
    q = 149
    # encryption exponent e
    e = 257
    # encrypted message r
    r = 1907
    print("Running RSA Algorithms to find the RSA Modulus (n), the decryption exponent (d), and the decrypted message (s) for the given input:")
    print('')
    print(f"first prime p: {p}")
    print(f"second prime q: {q}")
    print(f"encryption exponent e: {e}")
    print(f"encrypted message r: {r}")
    print("")
    print("Initializing RSA class with the given input...")

    test = RSA(p, q, e)

    n = test.getPublicKeyPair()[0]
    d = test._d
    s = test.decryptMessage(r)

    print("\nResults")
    print("~*" * 8)
    print(f"RSA Modulus n: {n}")
    print(f"Decryption exponent d (this should be private!): {d}")
    print(f"Decrypted message s: {s}")
    print(f"n, d, s = {n}, {d}, {s}")
    print("~*" * 8)


if __name__ == "__main__":
    main()
