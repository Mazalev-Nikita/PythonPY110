import json


def task():
    filename = "input.json"
    with open(filename) as f:
        a = json.load(f)

    return max(a, key=lambda item: item["score"])


if __name__ == "__main__":
    print(task())
