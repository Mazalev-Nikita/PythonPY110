from itertools import repeat


def task():
    a = 10
    # b = print(list(repeat(a, 4)))

    for num in repeat(a, 4):  # TODO повторить переменную a 4 раза
       print(num)


if __name__ == "__main__":
    task()
