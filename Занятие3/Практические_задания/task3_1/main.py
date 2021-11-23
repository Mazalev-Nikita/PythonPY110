import pickle


def some_func():
    print("Hello, World")


def to_pickle_file(obj, filename: str) -> None:
    if not filename.endswith('.pickle'):
        filename += '.pickle'

    with open(filename, "w") as f:
        pickle.dump(obj, f)


def from_pickle_file(filename: str):
    with open(filename, "r") as f:
        obj = pickle.load(f)

    return obj


if __name__ == "__main__":
    dict_pickle = {
        1: 1,
        "2": 5,
        (5, 7): "test",
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
        "func": some_func
    }

    to_pickle_file(dict_pickle, "output")  # записываем объект в файл
    obj_from_file = from_pickle_file("output.pickle")  # считываем объект из файла

    obj_from_file["func"]()
    print(dict_pickle)# вызываем функцию из словаря
