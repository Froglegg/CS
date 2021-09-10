import string

lowercase_alphabet = string.ascii_lowercase
alphabet_cipher = {}

for idx, l in enumerate(lowercase_alphabet):
    alphabet_cipher[l] = f"{idx+1:02}"
    alphabet_cipher[f"{idx+1:02}"] = l


def convert_word_to_int(word: str) -> int:
    int_string = ""
    for c in word:
        int_string += alphabet_cipher[c.lower()]
    return int(int_string.ljust(6, "0"))
