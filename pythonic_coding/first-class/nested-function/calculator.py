#!/usr/bin/python3


def calculator(x):

    def add(y):
        return x + y

    return add


if __name__ == "__main__":
    f = calculator(10)  # f is assigned to add function
    print(f(5))  # output: 15
    print(f(10))  # output: 20
