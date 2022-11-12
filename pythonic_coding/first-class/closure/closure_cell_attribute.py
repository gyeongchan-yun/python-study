#!/usr/bin/python3


def closure():
    x = 10

    def inner():
        y = 20
        return x + y

    return inner


if __name__ == "__main__":
    c = closure()

    print("== closure attribute == ")
    print("number of tuple: {}".format(len(c.__closure__)))
    print(dir(c.__closure__[0]))
    print(c.__closure__[0].cell_contents)
