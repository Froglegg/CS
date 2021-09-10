# experimenting with these helper functions

def string_list_to_binary(lyst=["xyz", "abc"]) -> list:

    return [bin(int.from_bytes(i.encode(), "big")) for i in lyst]


def binary_list_to_string(binaryLyst) -> list[str]:

    string_lyst = []
    for i in binaryLyst:
        n = int(i, 2)
        n = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        string_lyst.append(n)

    return string_lyst


print(string_list_to_binary(["xyz", "abc"]))
