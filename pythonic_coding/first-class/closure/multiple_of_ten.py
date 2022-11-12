#!/usr/bin/python3


def multiple_of_ten():  # closure
    square_root = 10  # nonlocal variable

    def square(x):
        return square_root ** x

    return square


def main():
    f = multiple_of_ten()
    print(f(2))
    print(f(3))


if __name__ == "__main__":
    main()
