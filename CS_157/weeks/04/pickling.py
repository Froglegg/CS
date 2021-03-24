# hey
import pickle
obj = {
    "data1": "d1value",
    "data2": "d2value"
}

pickle.dump(obj, open("./save.p", "wb"))

unpickled = pickle.load(open("./save.p", "rb"))

print(unpickled)
